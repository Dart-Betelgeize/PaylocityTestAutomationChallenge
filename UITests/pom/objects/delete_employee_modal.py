from playwright.sync_api import Page

from pom.objects.base_modal import BaseModal

class DeleteEmployeeModal(BaseModal):
    def __init__(self, page: Page):
        super().__init__(page)
        self.message = self.modal.locator('//*[@class="row"]')
        self.delete_button = self.modal.locator('//*[@id="deleteEmployee"]')
        self.modal_title = self.modal.locator('h5.modal-title:has-text("Delete Employee")')

    def get_message(self):
        self.message.inner_text()