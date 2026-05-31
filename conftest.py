import allure
import pytest
from playwright.sync_api import Page, expect

from page_object import LoginPage


@pytest.fixture()
def start_page (page: Page):
    page.goto("http://litres.ru", wait_until="domcontentloaded")

    return page

@pytest.fixture()
def authorized_page (start_page: Page):
    with allure.step("Авторизация"):
        login_page = LoginPage (start_page)
        login_page.do_login()
        return start_page

@pytest.fixture()
def clear_cart (authorized_page: Page):
    clear_the_cart(authorized_page)
    yield authorized_page
    clear_the_cart(authorized_page)


def clear_the_cart (page: Page):
    page.goto("http://litres.ru/my-books/cart/", wait_until="domcontentloaded")
    cart_items = page.locator('[data-testid^="cart__listItem--"]')
    delete_buttons = page.get_by_test_id("cart__listDeleteButton")
    confirm_delete = page.get_by_test_id("cart__modalDeleteArt--button-primary")

    while cart_items.count() > 0:
        count_before = cart_items.count()

        delete_buttons.first.click()
        confirm_delete.click()

        expect(cart_items).to_have_count(count_before - 1)



