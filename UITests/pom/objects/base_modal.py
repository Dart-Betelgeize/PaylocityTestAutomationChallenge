from playwright.sync_api import Page

class BaseModal:
    def __init__(self, page: Page):
        self.page = page
        self.modal = self.page.locator('.modal-content')
        self.modal_title = self.modal.locator('.modal-title')
        self.close_button = self.modal.get_by_role("button", name="Close")
        self.cancel_button = self.modal.get_by_role("button", name="Cancel")

    def close(self):
        self.close_button.click()

    def get_title(self):
        return self.modal_title.inner_text()