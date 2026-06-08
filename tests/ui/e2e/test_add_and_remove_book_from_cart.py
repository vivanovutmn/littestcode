import allure
from playwright.sync_api import expect
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from pages.book_page import BookPage
from data_test_files.test_data import TestBook

@allure.feature("Корзина")
@allure.story("Добавление и удаление книги")
@allure.title("Пользователь может добавить книгу в корзину и удалить её")
def test_add_del_book (authorized_empty_cart_page, opened_book_page):
    # with allure.step("Поиск книги"):
    #     search_page = SearchPage (authorized_empty_cart_page)
    #     search_page.search_book(TestBook.search_text)
    # with allure.step("Открытие найденной книги"):
    #     book_page = search_page.open_book (TestBook.card_name)
    with allure.step("Добавление книги в корзину"):
        opened_book_page.add_book()
    with allure.step("Удаление книги из корзины"):
        cart_page = CartPage (opened_book_page.page)
        cart_page.delete_book_by_name(TestBook.cart_title)
    with allure.step("Проверить, что корзина пустая"):
        expect(cart_page.happy_path).to_be_visible(timeout=15000)
    with allure.step ("Проверить, что книгу снова можно добавить в корзину после удаления из нее"):
        opened_book_page.page.go_back()
        expect(opened_book_page.page.get_by_test_id("book__addToCartButton")).to_be_visible()





