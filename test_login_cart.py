import re
from playwright.sync_api import Page, expect, TimeoutError
import pytest
from logi_cart_page import LoginPage, SearchPage, BookPage, CartPage

# def test_example(page: Page) -> None:
#     page.goto("http://litres.ru")
#     page.get_by_test_id("tab-login").get_by_test_id("tab__link").click()
#     page.get_by_test_id("auth__input--enterEmailOrLogin").click()
#     page.get_by_test_id("auth__input--enterEmailOrLogin").fill("ehome.qqq@gmail.com")
#     page.get_by_test_id("auth__button--continue").click()
#     page.get_by_test_id("input__field").get_by_text("Пароль").click()
#     page.get_by_test_id("auth__input--enterPassword").click()
#     page.get_by_test_id("auth__input--enterPassword").fill("1649218#Dom")
#     page.get_by_test_id("auth__button--enter").click()
#     page.get_by_test_id("search__input").click()
#     page.get_by_test_id("search__input").fill("Ведьмак")
#     page.get_by_test_id("search__input").press("Enter")
#     page.goto("https://www.litres.ru/search/?q=%D0%92%D0%B5%D0%B4%D1%8C%D0%BC%D0%B0%D0%BA")
#     page.get_by_test_id("cookieAcceptPopup__accept").click()
#     with page.expect_popup() as page1_info:
#         page.get_by_role("group", name="Ведьмак в озвучке Всеволода Кузнецова. Анджей Сапковский. Аудио. Хит продаж").get_by_test_id("art__cover").click()
#     page1 = page1_info.value
#     page1.get_by_test_id("book__addToCartButton").click()
#     page1.get_by_role("button", name="Закрыть").click()
#     page1.get_by_test_id("book__goToCartButton").click()
#     page1.get_by_test_id("cart__listItem--70548067").get_by_test_id("cart__listDeleteButton").click()
#     page1.get_by_test_id("cart__modalDeleteArt--button-primary").click()
#     expect(page.get_by_text ("Ведьмак в озвучке Всеволода Кузнецова. Анджей Сапковский. Аудио. Хит продаж")).not_to_be_visible()
def test_add_book (start_page):
    login_page = LoginPage (start_page)
    login_page.do_login()

    search_page = SearchPage (start_page)
    search_page.search_book("Ведьмак")

    book_page = search_page.open_book ("Ведьмак в озвучке Всеволода Кузнецова. Анджей Сапковский. Аудио. Хит продаж")
    book_page_object = BookPage (book_page)
    book_page_object.add_book()

    cart_page = CartPage (book_page)
    cart_page.del_book()
    expect(cart_page.happy_path).to_be_visible()





