
from playwright.sync_api import sync_playwright, expect
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Route Telegram API requests to mock success
    def handle_telegram_route(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"ok": true, "result": {}}'
        )

    page.route("https://api.telegram.org/**", handle_telegram_route)

    # 1. Navigate to index.html
    print("Navigating to index.html...")
    page.goto("http://localhost:8000/index.html")

    # 2. Find and click the 'Check Your Eligibility Now' link
    print("Clicking eligibility link...")
    # Using text or href to locate the button/link
    eligibility_link = page.get_by_role("link", name="Check Your Eligibility Now")
    eligibility_link.click()

    # 3. Verify navigation to eligibility.html
    print("Verifying navigation...")
    expect(page).to_have_url("http://localhost:8000/eligibility.html")

    # 4. Fill out the form
    print("Filling out the form...")
    page.fill("#name", "Test User")
    page.fill("#email", "test@example.com")
    page.fill("#phone", "+1234567890")
    page.select_option("#nationality", "Indian")
    page.fill("#physics", "70")
    page.fill("#chemistry", "70")
    page.fill("#biology", "70")
    page.fill("#neet", "150") # Eligible (>137) and PCB > 60

    # 5. Submit the form
    print("Submitting form...")
    page.click("#submitFormBtn")

    # 6. Verify success message
    print("Verifying success message...")
    result_div = page.locator("#eligibilityResult")
    expect(result_div).to_be_visible()
    expect(result_div).to_contain_text("Congratulations Test User! You are eligible")

    # Take screenshot
    page.screenshot(path="verification/verification.png")
    print("Verification complete. Screenshot saved.")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
