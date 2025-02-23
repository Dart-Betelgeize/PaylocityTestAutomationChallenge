import random
import pytest

from utils.test_data_generator import TestDataGenerator
from UITests.utils.constants import DASHBOARD_TITLE
from UITests.utils.constants import TABLE_HEADERS

def test_dashboard_page_content(dashboard):
    # Then
    dashboard.check_page_title_is_correct(DASHBOARD_TITLE)
    dashboard.check_table_exists()
    dashboard.check_table_headers_are_correct(TABLE_HEADERS)
    dashboard.check_add_employee_button()
    dashboard.check_log_out_button_exists()
    dashboard.check_footer_content_is_correct()