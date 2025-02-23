from utils.test_data_generator import TestDataGenerator
from utils.constants import DASHBOARD_TITLE
from utils.constants import TABLE_HEADERS

def test_add_new_employee_modal_content(dashboard):
    # When
    dashboard.open_add_employee_modal()
    # Then
    dashboard.add_employee_keywords.check_modal_title_is_correct("Add Employee")
    dashboard.add_employee_keywords.check_modal_fields()
    dashboard.add_employee_keywords.check_add_modal_button()
    dashboard.add_employee_keywords.check_cancel_modal_button()
    dashboard.add_employee_keywords.check_close_button_exists()

# Here we could add more tests like:
# - Close button should close the modal, no employee created
# - Cancel button should close the modal, no employee created
# - Click outside the modal should close the modal, no employee created
# - Click add should close the modal, employee is created
# - Fields validations tests
# etc... I will skip these tests in this challenge due of lack of time