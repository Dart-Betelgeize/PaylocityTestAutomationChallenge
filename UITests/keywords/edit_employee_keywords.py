from playwright.sync_api import expect
from pom.objects.edit_employee_modal import EditEmployeeModal

class EditEmployeeKeywords:
    def __init__(self, edit_employee_modal: EditEmployeeModal):
        self.edit_employee_modal = edit_employee_modal

    def edit_employee(self, first_name: str, last_name: str, dependents: int):
        self.edit_employee_modal.fill_employee_details(first_name, last_name, dependents)
        self.edit_employee_modal.update_button.click()
