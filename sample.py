from playwright import sync_api

with sync_api.sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://quesada.tacitdev.ca/")
    assert page.title() == 'Quesada'




