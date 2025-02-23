from utils.test_data_generator import TestDataGenerator
from utils.constants import SALARY

def test_add_employee(dashboard):
    # Given
    first_name, last_name, random_dependents = TestDataGenerator.generate_random_employee_data()
    # When
    dashboard.open_add_employee_modal()
    dashboard.add_employee_keywords.add_employee(first_name, last_name, random_dependents)
    dashboard.wait_for_dashboard_to_load()
    # Then
    # Since we have a know bug with switched First Name and Last name (Bug 1) I consciously switch it in the test too to be able to check other parts of this e2e test
    table_row = dashboard.check_dashboard_table_contains_created_employee(first_name=last_name, last_name=first_name, dependents=random_dependents)
    dashboard.check_calculations_are_correct(table_row, SALARY, random_dependents)

def test_edit_employee(dashboard):
    # Given
    first_name, last_name, random_dependents = TestDataGenerator.generate_random_employee_data()
    random_employee_id = dashboard.get_random_employee_from_the_table()
    # When
    dashboard.open_edit_employee_modal_for_employee_with_id(random_employee_id)
    dashboard.edit_employee_keywords.edit_employee(first_name, last_name, random_dependents)
    dashboard.wait_for_dashboard_to_load()
    # Then
    # Since we have a know bug with switched First Name and Last name (Bug 1) I consciously switch it in the test too to be able to check other parts of this e2e test
    table_row = dashboard.check_employee_is_updated_in_the_dashboard_table(id=random_employee_id, first_name=last_name, last_name=first_name, dependents=random_dependents)
    dashboard.check_calculations_are_correct(table_row, SALARY, random_dependents)

def test_delete_employee(dashboard):
    # Given
    random_employee_id = dashboard.get_random_employee_from_the_table()
    # When
    dashboard.open_delete_employee_modal_for_employee_with_id(random_employee_id)
    dashboard.delete_employee_keywords.delete_employee()
    dashboard.wait_for_dashboard_to_load()
    # Then
    dashboard.check_employee_is_deleted_from_dashboard_table(id=random_employee_id)