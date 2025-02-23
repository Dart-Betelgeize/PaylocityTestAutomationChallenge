from utils.test_data_generator import TestDataGenerator
from utils.constants import DASHBOARD_TITLE
from utils.constants import TABLE_HEADERS

def test_dashboard_page_content(dashboard):
    # Then
    dashboard.check_page_title_is_correct(DASHBOARD_TITLE)
    dashboard.check_table_exists()
    dashboard.check_add_employee_button()
    dashboard.check_log_out_button_exists()
    dashboard.check_footer_content_is_correct()

def test_dashboard_table_content(dashboard):
    # Then
    dashboard.check_table_headers_are_correct(TABLE_HEADERS)
    dashboard.check_employee_has_actions_buttons()

# Here we could add more tests like:
# - Log out link check
# - Page refresh
# - Probably we can move calculations checks from e2e tests to functional
# - We can test table sorting
# - We can test format of values in the table
# etc... I will skip these tests in this challenge due of lack of time