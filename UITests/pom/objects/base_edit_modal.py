from playwright.sync_api import Page

from pom.objects.base_modal import BaseModal

class BaseEditModal(BaseModal):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = self.modal.locator('//*[@id="firstName"]')
        self.last_name_input = self.modal.locator('//*[@id="lastName"]')
        self.dependants_input = self.modal.locator('//*[@id="dependants"]')
    
    def fill_employee_details(self, first_name: str, last_name: str, dependents: int):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.dependants_input.fill(str(dependents))