from playwright.sync_api import sync_playwright

def before_all(context):
    print("Initializing Playwright...")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    print("Playwright initialized. Browser and page are ready.")

def after_all(context):
    print("Closing Playwright...")
    context.browser.close()
    context.playwright.stop()
    print("Playwright closed.")

