from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)

    def get_browser(self):
        return self.browser

    def stop(self):
        self.browser.close()
        self.playwright.stop()
