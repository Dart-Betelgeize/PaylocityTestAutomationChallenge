from playwright.sync_api import Page

from pom.objects.base_edit_modal import BaseEditModal

class AddEmployeeModal(BaseEditModal):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_button = self.modal.locator('//*[@id="addEmployee"]')
        self.modal_title = self.modal.locator('h5.modal-title:has-text("Add Employee")')