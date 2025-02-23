import random
from pom.dashboard_page import DashboardPage
from pom.objects.add_employee_modal import AddEmployeeModal
from pom.objects.delete_employee_modal import DeleteEmployeeModal
from pom.objects.edit_employee_modal import EditEmployeeModal
from pom.objects.table_row import TableRow

class DashboardKeywords:
    def __init__(self, dashboard_page: DashboardPage):
        self.dashboard_page = dashboard_page

    def add_employee(self, first_name: str, last_name: str, dependents: int):
        self.dashboard_page.add_employee_button.click()
        add_employee_modal = AddEmployeeModal(self.dashboard_page.page)
        add_employee_modal.first_name_input.fill(first_name)
        add_employee_modal.last_name_input.fill(last_name)
        add_employee_modal.dependants_input.fill(str(dependents))
        add_employee_modal.add_button.click()
        self.dashboard_page.wait_for_table_to_be_loaded()


    def check_dashboard_table_contains_created_employee(self, first_name: str, last_name: str, dependents: int):
        table_row = self.dashboard_page.get_table_row_by_full_employee_name(first_name, last_name)
        assert table_row is not None, f"Employee {first_name} {last_name} not found in the table"
        # Not the best solution to hardcode here the column name, could be improved later
        actual_dependent_value = int(self.dashboard_page.get_column_value_in_the_row(table_row, "Dependents"))
        assert actual_dependent_value == dependents, f"Dependents value is wrong"
        return table_row
    
    def check_calculations_are_correct(self, table_row: TableRow, expected_salary: int, dependents: int):
        # Not the best solution to hardcode here the column name, could be improved later
        salary = float(self.dashboard_page.get_column_value_in_the_row(table_row, "Salary"))
        gross_pay = float(self.dashboard_page.get_column_value_in_the_row(table_row, "Gross Pay"))
        benefits_cost = float(self.dashboard_page.get_column_value_in_the_row(table_row, "Benefits Cost"))
        net_pay = float(self.dashboard_page.get_column_value_in_the_row(table_row, "Net Pay"))
        assert salary == float(expected_salary), f"Salary calculation is wrong"
        assert gross_pay == float(salary/26), f"Gross Pay calculation is wrong"
        assert benefits_cost == round(float(1000/26+500/26*dependents), 2), f"Benefits Cost calculation is wrong"
        assert net_pay == gross_pay-benefits_cost, f"Net Pay calculation is wrong"

    def get_random_employee_from_the_table(self):
        self.dashboard_page.wait_for_table_to_be_loaded()
        rows_count = self.dashboard_page.get_table_rows_count()
        random_row_index = random.randint(0, rows_count-1)
        row = self.dashboard_page.get_row(random_row_index)
        return self.dashboard_page.get_column_value_in_the_row(row, "Id")
    
    def update_employee(self, id: str, first_name: str, last_name: str, dependents: int):
        row = self.dashboard_page.get_table_row_by_id(id)
        row.edit_employee_button.click()
        edit_employee_modal = EditEmployeeModal(self.dashboard_page.page)
        edit_employee_modal.first_name_input.fill(first_name)
        edit_employee_modal.last_name_input.fill(last_name)
        edit_employee_modal.dependants_input.fill(str(dependents))
        edit_employee_modal.update_button.click()
        self.dashboard_page.wait_for_table_to_be_loaded()

    def check_employee_is_updated_in_the_dashboard_table(self, id: str, first_name: str, last_name: str, dependents: int):
        table_row = self.dashboard_page.get_table_row_by_id(id)
        assert table_row is not None, f"Employee not found in the table"
        # Not the best solution to hardcode here the column name, could be improved later
        actual_dependent_value = int(self.dashboard_page.get_column_value_in_the_row(table_row, "Dependents"))
        actual_first_name = self.dashboard_page.get_column_value_in_the_row(table_row, "First Name")
        actual_last_name = self.dashboard_page.get_column_value_in_the_row(table_row, "Last Name")
        assert actual_first_name == first_name, f"First Name value is wrong"
        assert actual_last_name == last_name, f"Last Name value is wrong"
        assert actual_dependent_value == dependents, f"Dependents value is wrong"
        return table_row
    
    def delete_employee(self, id: str):
        row = self.dashboard_page.get_table_row_by_id(id)
        row.delete_employee_button.click()
        delete_employee_modal = DeleteEmployeeModal(self.dashboard_page.page)
        delete_employee_modal.delete_button.click()
        self.dashboard_page.wait_for_table_to_be_loaded()

    def check_employee_is_deleted_from_dashboard_table(self, id: str):
        table_row = self.dashboard_page.get_table_row_by_id(id)
        assert table_row is None, f"Employee still exists in the table"

    def check_page_title_is_correct(self, expected_title: str):
        assert self.dashboard_page.get_title() == expected_title, f"Page title is wrong"

    def check_table_exists(self):
        assert self.dashboard_page.table.is_visible(), f"Table is not visible"

    def check_table_headers_are_correct(self, expected_headers):
        headers = self.dashboard_page.get_table_header_texts()
        assert headers == expected_headers, f"Table headers are not correct"

    def check_add_employee_button(self):
        assert self.dashboard_page.add_employee_button.is_visible(), f"Add Employee button is not visible"
        assert self.dashboard_page.add_employee_button.inner_text() == "Add Employee" , f"Add Employee button text is wrong"

    def check_log_out_button_exists(self):
        assert self.dashboard_page.log_out_link.is_visible(), f"Log out button is not visible"

    def check_log_out_button_exists(self):
        assert self.dashboard_page.log_out_link.is_visible(), f"Log out button is not visible"

    def check_footer_content_is_correct(self):
        assert self.dashboard_page.footer.inner_text == "© 2025 - Paylocity", f"Footer content is wrong"