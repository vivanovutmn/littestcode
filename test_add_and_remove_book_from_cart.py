import allure
from playwright.sync_api import expect
from page_object import SearchPage, BookPage, CartPage
from test_data import TestBook

@allure.feature("Корзина")
@allure.story("Добавление и удаление книги")
@allure.title("Пользователь может добавить книгу в корзину и удалить её")
def test_add_del_book (authorized_page):
    with allure.step("Поиск книги"):
        search_page = SearchPage (authorized_page)
        search_page.search_book(TestBook.search_text)
    with allure.step("Открытие найденной книги"):
        book_page = search_page.open_book (TestBook.card_name)
        book_page_object = BookPage (book_page)
    with allure.step("Добавление книги в корзину"):
        book_page_object.add_book()
    with allure.step("Удаление книги из корзины"):
        cart_page = CartPage (book_page)
        cart_page.delete_book_by_name(TestBook.card_name)
    with allure.step("Проверить, что корзина пустая"):
        expect(cart_page.happy_path).to_be_visible()





