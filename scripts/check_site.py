"""Browser smoke check; no network services or project builds are needed."""

import functools
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import threading

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / ".preview"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def contrast(first, second):
    def luminance(value):
        channels = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels]
        return sum(c * weight for c, weight in zip(linear, (.2126, .7152, .0722)))

    light, dark = sorted((luminance(first), luminance(second)), reverse=True)
    return (light + .05) / (dark + .05)


def main():
    OUTPUT.mkdir(exist_ok=True)
    checks = []
    tokens = dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6});", (ROOT / "styles.css").read_text()))
    pairs = [
        ("ink", "canvas"), ("muted", "canvas"), ("accent", "canvas"),
        ("muted", "surface"), ("accent", "surface"), ("canvas", "ink"),
        ("inverse-muted", "ink"), ("inverse-accent", "ink"),
        ("muted", "accent-soft"), ("accent", "accent-soft"),
    ]
    for foreground, background in pairs:
        name = f"{foreground}/{background}"
        ratio = contrast(tokens[foreground], tokens[background])
        assert ratio >= 4.5, f"Insufficient contrast for {name}: {ratio}"
        checks.append({"check": name, "contrast": round(ratio, 2)})
    diagram_ratio = contrast(tokens["inverse-line"], tokens["ink"])
    assert diagram_ratio >= 3, "Insufficient diagram line contrast"
    checks.append({"check": "diagram-lines/ink", "contrast": round(diagram_ratio, 2)})

    handler = functools.partial(QuietHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    origin = f"http://127.0.0.1:{server.server_port}"
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel="chrome", headless=True)
            for width, height in [(1440, 1000), (1024, 900), (768, 1024), (390, 844), (320, 720)]:
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    device_scale_factor=1,
                    java_script_enabled=False,
                    reduced_motion="reduce",
                )
                page = context.new_page()
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                response = page.goto(origin, wait_until="networkidle")
                assert response.status == 200
                page.evaluate("document.fonts.ready")
                assert page.evaluate("document.fonts.check('16px \"Public Sans\"')")
                assert page.evaluate("document.fonts.check('48px Newsreader')")
                assert page.locator("h1").count() == 1
                assert page.locator("article").count() == 2
                assert page.locator("html").get_attribute("lang") == "en"
                assert page.title() == "Mehdi Benbarka — AI & software projects"
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Overflow at {width}px"
                assert page.evaluate("""() => {
                    const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
                    return new Set(ids).size === ids.length;
                }"""), "Duplicate IDs"
                for link in page.locator('a[href^="#"]').all():
                    fragment = link.get_attribute("href")
                    assert len(fragment) > 1 and page.locator(fragment).count() == 1, fragment

                page.keyboard.press("Tab")
                assert page.locator(".skip-link").evaluate("el => el === document.activeElement")
                page.keyboard.press("Enter")
                assert page.url.endswith("#main")

                for detail in page.locator("details").all():
                    assert not detail.evaluate("el => el.open")
                    detail.locator("summary").focus()
                    page.keyboard.press("Enter")
                    assert detail.evaluate("el => el.open")
                    assert detail.locator(".detail-content").is_visible()
                    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
                    page.keyboard.press("Enter")
                    assert not detail.evaluate("el => el.open")

                page.locator('label[for="view-rejected"]').click()
                assert page.locator("#view-rejected").is_checked()
                assert page.locator(".panel-rejected").is_visible()
                assert not page.locator(".panel-pending").is_visible()
                page.locator("#view-rejected").focus()
                page.keyboard.press("ArrowRight")
                assert page.locator("#view-applied").is_checked()
                assert page.locator(".panel-applied").is_visible()
                assert not page.locator(".panel-rejected").is_visible()
                page.locator('label[for="view-pending"]').click()
                assert page.locator(".panel-pending").is_visible()
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")

                page.get_by_role("navigation").get_by_role("link", name="About").click()
                assert page.url.endswith("#about")
                page.get_by_role("link", name="Back to top").click()
                assert page.url.endswith("#top")
                page.locator("body").click(position={"x": 2, "y": 2})
                page.screenshot(path=str(OUTPUT / f"portfolio-{width}.png"), full_page=True)
                assert not errors, errors
                checks.append({"check": f"browser-{width}", "status": "passed", "javascript": "disabled"})
                response = page.goto(origin + "/404.html")
                assert response.status == 200
                page.get_by_role("link", name="Back to the portfolio").click()
                assert page.url == origin + "/"
                context.close()
            context = browser.new_context(java_script_enabled=False, reduced_motion="reduce")
            page = context.new_page()
            page.goto(origin, wait_until="networkidle")
            for width in [360, 420, 421, 640, 760, 761, 900, 1100, 1101, 1280, 1920]:
                page.set_viewport_size({"width": width, "height": 900})
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Overflow at breakpoint {width}"
            checks.append({"check": "responsive-breakpoints", "status": "passed"})
            context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()

    (OUTPUT / "checks.json").write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "checks": checks, "screenshots": str(OUTPUT)}, indent=2))


if __name__ == "__main__":
    main()
