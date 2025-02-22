import pytest

EXPECTED_URL = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Benefits"

def test_valid_login(logged_in_page):
    logged_in_page.wait_for_load_state("domcontentloaded")
    assert logged_in_page.url == EXPECTED_URL