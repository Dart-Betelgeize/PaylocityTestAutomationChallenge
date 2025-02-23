import pytest
from utils.env_data import DASHBOARD_URL

def test_valid_login(logged_in_page):
    logged_in_page.wait_for_load_state("domcontentloaded")
    # Then
    assert logged_in_page.url == DASHBOARD_URL