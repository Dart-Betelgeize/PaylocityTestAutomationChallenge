from playwright.sync_api import expect
from pom.objects.add_employee_modal import AddEmployeeModal

class AddEmployeeKeywords:
    def __init__(self, add_employee_modal: AddEmployeeModal):
        self.add_employee_modal = add_employee_modal

    def add_employee(self, first_name: str, last_name: str, dependents: int):
        self.add_employee_modal.fill_employee_details(first_name, last_name, dependents)
        self.add_employee_modal.add_button.click()

    def check_modal_title_is_correct(self, expected_title: str):
        expect(self.add_employee_modal.modal_title).to_have_text(expected_title)

    def check_modal_fields(self):
        pass

    def check_add_modal_button(self):
        add_button = self.add_employee_modal.add_button
        expect(add_button).to_be_visible()
        expect(add_button).to_have_text("Add")

    def check_cancel_modal_button(self):
        cancel_button = self.add_employee_modal.cancel_button
        expect(cancel_button).to_be_visible()
        expect(cancel_button).to_have_text("Cancel")

    def check_close_button_exists(self):
        expect(self.add_employee_modal.close_button).to_be_visible()
