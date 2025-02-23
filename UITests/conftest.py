import pytest
from playwright.sync_api import sync_playwright
from keywords.dashboard_keywords import DashboardKeywords
from pom.dashboard_page import DashboardPage
from pom.login_page import LoginPage
from utils.env_data import USERNAME
from utils.env_data import PASSWORD

# Launch browser once per sessions
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

# Create new page per test
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

# Login fixture
@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    yield page

@pytest.fixture(scope="function")
def dashboard(logged_in_page):
    # Fixture to provide DashboardKeywords instance.
    dashboard_page = DashboardPage(logged_in_page)
    dashboard = DashboardKeywords(dashboard_page)
    logged_in_page.wait_for_load_state("domcontentloaded")  # Ensure the page is fully loaded
    return dashboard