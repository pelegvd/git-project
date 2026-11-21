import re
from playwright.sync_api import Page, expect

def test_playwright_homepage_navigation(page: Page):
    # 1. ניווט לאתר הרשמי של Playwright
    page.goto("https://playwright.dev/")

    # 2. אימות כותרת העמוד
    expect(page).to_have_title(re.compile("Playwright"))

    # 3. לחיצה על כפתור Get started ואימות המעבר לעמוד ההתקנה
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
