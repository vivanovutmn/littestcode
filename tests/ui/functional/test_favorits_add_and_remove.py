# import allure
# from playwright.sync_api import expect
# from page_object import SearchPage, BookPage
# from test_datas import TestBook
# @allure.feature("Отложенное")
# @allure.story("Добавление и удаление книги")
# @allure.title("Пользователь может добавить книгу в отложенное и удалить её")
# def test_add_del_book (authorized_empty_cart_page):
#     with allure.step("Поиск книги"):
#         search_page = SearchPage (authorized_empty_cart_page)
#         search_page.search_book(TestBook.search_text)
#     with allure.step("Открытие найденной книги"):
#         book_page = search_page.open_book (TestBook.card_name)
#         book_page_object = BookPage (book_page)
#     with allure.step("Добавление книги в отложенное"):
#             book_page_object.add_to_favorites()
#             book_page_object.should_be_in_favorites()
#     with allure.step("Удаление книги из отложенного"):
#         book_page_object.remove_from_favorites()
#         book_page_object.should_not_be_in_favorites()

import allure
from pages.search_page import SearchPage
from pages.book_page import BookPage
from data_test_files.test_data import TestBook


# @allure.feature("Отложенное")
# @allure.story("Добавление и удаление книги")
# @allure.title("Пользователь может добавить книгу в отложенное и удалить её")
# def test_add_and_remove_book_from_favorites(authorized_page):
#     with allure.step("Поиск книги"):
#         search_page = SearchPage(authorized_page)
#         search_page.search_book(TestBook.search_text)
#
#     with allure.step("Открытие найденной книги"):
#         book_page = search_page.open_book(TestBook.card_name)
#         book_page_object = BookPage(book_page)
#
#     with allure.step("Добавление книги в отложенное"):
#         book_page_object.add_to_favorites()
#         book_page_object.should_be_in_favorites()
#
#     with allure.step("Удаление книги из отложенного"):
#         book_page_object.remove_from_favorites()
#         book_page_object.should_not_be_in_favorites()

import allure


@allure.feature("Отложенное")
@allure.story("Добавление и удаление книги")
@allure.title("Пользователь может добавить книгу в отложенное и удалить её")
def test_add_and_remove_book_from_favorites(opened_book_page):
    with allure.step("Добавление книги в отложенное"):
        opened_book_page.add_to_favorites()

    with allure.step("Удаление книги из отложенного"):
        opened_book_page.remove_from_favorites()