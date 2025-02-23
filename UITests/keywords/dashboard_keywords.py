import random
import re
from playwright.sync_api import expect
from keywords.add_employee_keywords import AddEmployeeKeywords
from keywords.delete_employee_keywords import DeleteEmployeeKeywords
from keywords.edit_employee_keywords import EditEmployeeKeywords
from pom.dashboard_page import DashboardPage
from pom.objects.add_employee_modal import AddEmployeeModal
from pom.objects.delete_employee_modal import DeleteEmployeeModal
from pom.objects.edit_employee_modal import EditEmployeeModal
from pom.objects.table_row import TableRow

class DashboardKeywords:
    def __init__(self, dashboard_page: DashboardPage):
        self.dashboard_page = dashboard_page
    
    @property
    def add_employee_keywords(self):
        # Return an instance of AddEmployeeKeywords
        return AddEmployeeKeywords(self._get_add_employee_modal())
    
    @property
    def edit_employee_keywords(self):
        # Return an instance of AddEmployeeKeywords
        return EditEmployeeKeywords(self._get_edit_employee_modal())
    
    @property
    def delete_employee_keywords(self):
        # Return an instance of AddEmployeeKeywords
        return DeleteEmployeeKeywords(self._get_delete_employee_modal())

    def _get_add_employee_modal(self):
        return AddEmployeeModal(self.dashboard_page.page)
    
    def _get_edit_employee_modal(self):
        return EditEmployeeModal(self.dashboard_page.page)
    
    def _get_delete_employee_modal(self):
        return DeleteEmployeeModal(self.dashboard_page.page)

    def open_add_employee_modal(self):
        self.dashboard_page.add_employee_button.click()

    def wait_for_dashboard_to_load(self):
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

        assert salary == float(expected_salary), f"Expected salary to be {expected_salary}, but got {salary}"
        assert gross_pay == float(salary / 26), f"Expected gross pay to be {salary / 26}, but got {gross_pay}"
        assert benefits_cost == round(float(1000 / 26 + 500 / 26 * dependents), 2), f"Expected benefits cost to be {round(float(1000 / 26 + 500 / 26 * dependents), 2)}, but got {benefits_cost}"
        assert net_pay == gross_pay - benefits_cost, f"Expected net pay to be {gross_pay - benefits_cost}, but got {net_pay}"

    def get_random_employee_from_the_table(self):
        # This method should be refactored later to check if table is not empty
        self.dashboard_page.wait_for_table_to_be_loaded()
        rows_count = self.dashboard_page.get_table_rows_count()
        random_row_index = random.randint(0, rows_count-1)
        row = self.dashboard_page.get_row(random_row_index)
        return self.dashboard_page.get_column_value_in_the_row(row, "Id")
    
    def open_edit_employee_modal_for_employee_with_id(self, id: str):
        row = self.dashboard_page.get_table_row_by_id(id)
        row.edit_employee_button.click()

    def check_employee_is_updated_in_the_dashboard_table(self, id: str, first_name: str, last_name: str, dependents: int):
        table_row = self.dashboard_page.get_table_row_by_id(id)
        assert table_row is not None, f"Employee not found in the table"

        # Not the best solution to hardcode here the column name, could be improved later
        actual_dependent_value = int(self.dashboard_page.get_column_value_in_the_row(table_row, "Dependents"))
        actual_first_name = self.dashboard_page.get_column_value_in_the_row(table_row, "First Name")
        actual_last_name = self.dashboard_page.get_column_value_in_the_row(table_row, "Last Name")

        assert actual_first_name == first_name, f"Expected first name to be '{first_name}', but got '{actual_first_name}'"
        assert actual_last_name == last_name, f"Expected last name to be '{last_name}', but got '{actual_last_name}'"
        assert actual_dependent_value == dependents, f"Expected dependents to be '{dependents}', but got '{actual_dependent_value}'"
        return table_row
    
    def open_delete_employee_modal_for_employee_with_id(self, id: str):
        row = self.dashboard_page.get_table_row_by_id(id)
        row.delete_employee_button.click()

    def check_employee_is_deleted_from_dashboard_table(self, id: str):
        table_row = self.dashboard_page.get_table_row_by_id(id)
        assert table_row is None, f"Employee still exists in the table"

    def check_page_title_is_correct(self, expected_title: str):
        expect(self.dashboard_page.title).to_have_text(expected_title)

    def check_table_exists(self):
        expect(self.dashboard_page.table).to_be_visible()

    def check_table_headers_are_correct(self, expected_headers):
        headers = self.dashboard_page.get_table_header_texts()
        assert headers == expected_headers, f"Expected headers {expected_headers}, but got {headers}"

    def check_add_employee_button(self):
        expect(self.dashboard_page.add_employee_button).to_be_visible()
        expect(self.dashboard_page.add_employee_button).to_have_text("Add Employee")

    def check_log_out_button_exists(self):
        expect(self.dashboard_page.log_out_link).to_be_visible()

    def check_footer_content_is_correct(self):
        expect(self.dashboard_page.footer).to_have_text(re.compile(r"©\s\d{4}\s-\sPaylocity"))

    def check_employee_has_actions_buttons(self):
        rows_count = self.dashboard_page.get_table_rows_count()
        assert rows_count > 0, "No rows found in the employee table."

        for i in range(rows_count):
            row = self.dashboard_page.get_row(i)
            expect(row.delete_employee_button).to_be_visible()
            expect(row.edit_employee_button).to_be_visible()

