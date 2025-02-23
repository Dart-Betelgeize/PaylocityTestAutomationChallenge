from playwright.sync_api import Page
from utils.env_data import LOGIN_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input[name='Username']"
        self.password_input = "input[name='Password']"
        self.login_button = "button[type='submit']"

    def navigate(self):
        self.page.goto(LOGIN_URL)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)