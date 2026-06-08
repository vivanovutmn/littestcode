from playwright.sync_api import Page, TimeoutError
from data_test_files.test_data import TestUser


class LoginPage:


    def __init__(self, page: Page):
        self.page = page
        self.login = page.get_by_test_id("tab-login").get_by_test_id("tab__link")
        self.login_input = self.page.get_by_test_id("auth__input--enterEmailOrLogin")
        self.login_button = self.page.get_by_test_id("auth__button--continue")
        self.password_input = self.page.get_by_test_id("auth__input--enterPassword")
        self.password_button = self.page.get_by_test_id("auth__button--enter")
        self.cookie_button = self.page.get_by_test_id("cookieAcceptPopup__accept")

    def do_login (self):
        self.login.click()
        self.login_input.fill(TestUser.login)
        self.login_button.click()
        self.password_input.fill(TestUser.password)
        self.password_button.click()
        try:
            self.cookie_button.click(timeout=3000)
        except TimeoutError:
            pass