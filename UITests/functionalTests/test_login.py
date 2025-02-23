from utils.env_data import DASHBOARD_URL

def test_valid_login(logged_in_page):
    logged_in_page.wait_for_load_state("domcontentloaded")
    # Then
    assert logged_in_page.url == DASHBOARD_URL

# Here we could add more tests for login like:
# - Login with invalid credentials -- > not loged in, check error message
# - Relogin
# etc... I will skip these tests in this challenge due of lack of time