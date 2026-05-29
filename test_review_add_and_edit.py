import allure
from page_object import SearchPage, BookPage
from test_data import TestBook, TestReview


@allure.feature("Отзывы")
@allure.story("Создание и редактирование отзыва")
@allure.title("Пользователь может оставить отзыв к книге и отредактировать его")
def test_add_edit_review(authorized_page):
    with allure.step("Поиск книги"):
        search_page = SearchPage(authorized_page)
        search_page.search_book(TestBook.search_text)

    with allure.step("Открытие найденной книги"):
        book_tab = search_page.open_book(TestBook.card_name)
        book_page = BookPage(book_tab)

    with allure.step("Публикация отзыва"):
        book_page.publish_review(TestReview.initial_text)

    with allure.step("Редактирование отзыва"):
        book_page.edit_review(TestReview.edited_text)