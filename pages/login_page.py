class LoginPage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username="Admin", password="admin123"):
        self.page.locator('input[name="username"]').fill(username)
        self.page.locator('input[name="password"]').fill(password)
        self.page.locator('button[type="submit"]').click()
