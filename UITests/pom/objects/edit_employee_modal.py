from playwright.sync_api import Page

from pom.objects.base_edit_modal import BaseEditModal

class EditEmployeeModal(BaseEditModal):
    def __init__(self, page: Page):
        super().__init__(page)
        self.update_button = self.modal.locator('//*[@id="updateEmployee"]')
        self.modal_title = self.modal.locator('h5.modal-title:has-text("Edit Employee")')