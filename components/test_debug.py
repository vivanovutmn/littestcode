import pytest
from playwright.sync_api import Page, expect
from pages.search_page import SearchPage
from pages.book_page import BookPage
from data_test_files.test_data import TestBook

def test_debug_page(authorized_page):
    search_page = SearchPage(authorized_page)
    search_page.search_book(TestBook.search_text)
    book_page = search_page.open_book(TestBook.card_name)

    # Ждём загрузки и смотрим все data-testid на странице
    book_page.wait_for_load_state("domcontentloaded")
    book_page.wait_for_timeout(3000)

    testids = book_page.locator("[data-testid]").all()
    for el in testids:
        tid = el.get_attribute("data-testid")
        print(f"testid: {tid}")

    # И отдельно — сколько wishlist-кнопок
    count = book_page.locator('[data-analytics-id="wishlist-button"]').count()
    print(f"wishlist buttons count: {count}")

    # Проверяем родителей первых нескольких wishlist-кнопок
    for i in range(min(count, 5)):
        btn = book_page.locator('[data-analytics-id="wishlist-button"]').nth(i)
        parent_testid = btn.locator("xpath=ancestor::*[@data-testid][1]").get_attribute("data-testid")
        print(f"wishlist button {i} — closest ancestor testid: {parent_testid}")