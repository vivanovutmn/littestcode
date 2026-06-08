from playwright.sync_api import Page, expect
from data_test_files.test_data import TestBook
class SearchPage:

    def __init__(self, page: Page):
        self.page = page
        self.search_input = self.page.get_by_test_id("search__input")

    def search_book (self, book_name: str):
        self.search_input.click()
        self.search_input.fill(book_name)
        self.search_input.press("Enter")
        expect(self.page.get_by_text(f"Результаты поиска «{TestBook.search_text}»")).to_be_visible()

    def open_book (self, book_card_name: str):
        book_card = self.page.get_by_role("group", name=book_card_name)
        with self.page.expect_popup() as popup_info:
            book_card.get_by_test_id ("art__cover").click()

        book_page = popup_info.value
        book_page.wait_for_load_state()
        return book_page