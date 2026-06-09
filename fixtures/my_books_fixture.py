import pytest
from playwright.sync_api import Page
from pages.my_books_page import MyBooksPage
@pytest.fixture()
def clear_favorite_list(page: Page):

    my_books_page = MyBooksPage(page)
    my_books_page.clear_favorites_list()

    yield
    my_books_page.clear_favorites_list()

