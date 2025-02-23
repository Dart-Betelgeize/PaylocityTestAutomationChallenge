from pom.objects.delete_employee_modal import DeleteEmployeeModal

class DeleteEmployeeKeywords:
    def __init__(self, delete_employee_modal: DeleteEmployeeModal):
        self.delete_employee_modal = delete_employee_modal

    def delete_employee(self):
        self.delete_employee_modal.delete_button.click()