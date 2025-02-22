from playwright.sync_api import Page

from pom.objects.base_modal import BaseModal

class AddEmployeeModal(BaseModal):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = self.modal.locator('//*[@id="firstName"]')
        self.last_name_input = self.modal.locator('//*[@id="lastName"]')
        self.dependants_input = self.modal.locator('//*[@id="dependants"]')
        self.add_button = self.modal.locator('//*[@id="addEmployee"]')