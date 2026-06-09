import pytest
from playwright.sync_api import Page, expect
from pages.search_page import SearchPage
from pages.book_page import BookPage
from data_test_files.test_data import TestBook

@pytest.fixture()
def opened_book_page (authorized_page: Page, clear_favorite_list):
    search_page = SearchPage (authorized_page)
    search_page.search_book(TestBook.search_text)

    book_page = search_page.open_book(TestBook.card_name)
    return BookPage (book_page)

@pytest.fixture()
def book_unread(opened_book_page: BookPage):
    if opened_book_page.unfinish_button.count() > 0:
        opened_book_page.unfinish_book()

    yield opened_book_page

    if opened_book_page.unfinish_button.count() > 0:
        opened_book_page.unfinish_book()

@pytest.fixture()
def book_unfavorites(opened_book_page: BookPage):
    if opened_book_page.fav_button.get_by_test_id("icon_favoritesFilled").count() > 0:
        opened_book_page.remove_from_favorites()
    yield opened_book_page

    if opened_book_page.fav_button.get_by_test_id("icon_favoritesFilled").count() > 0:
        opened_book_page.remove_from_favorites()
