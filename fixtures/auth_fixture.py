import allure
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture()
def start_page(page):
    page.goto("/", wait_until="domcontentloaded")
    return page


@pytest.fixture()
def authorized_page(start_page):
    return start_page

# @pytest.fixture()
# def start_page (page: Page):
#     page.goto("/", wait_until="domcontentloaded")
#
#     return page
#
# @pytest.fixture()
# def authorized_page (start_page: Page):
#     with allure.step("Авторизация"):
#         login_page = LoginPage (start_page)
#         login_page.do_login()
#
#     return start_page