class PimPage:
    def __init__(self, page):
        self.page = page

    def go_to_pim(self):
        self.page.locator('a[href="/web/index.php/pim/viewPimModule"]').click()

    def get_employee_names(self):
        self.page.wait_for_selector('//div[@class="oxd-table-card"]')
        return [
            el.inner_text()
            for el in self.page.locator('//div[@class="oxd-table-card"]//div[3]').all()
        ]