from playwright.sync_api import Page

class BaseModal:
    def __init__(self, page: Page):
        self.page = page
        self.modal = self.page.locator('//*[@class="modal-content"]')
        self.modal_title = self.modal.locator('//*[@class="modal-title"]')
        self.close_button = self.modal.locator('//*[@class="close"]')
        self.cancel_button = self.modal.locator('[class="btn-secondary"]')

    def close(self):
        self.close_button.click()

    def get_title(self):
        return self.modal_title.inner_text()