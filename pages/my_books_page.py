from playwright.sync_api import Page, expect

class MyBooksPage:
    def __init__(self, page: Page):
        self.page = page
        self.my_books_button = page.get_by_test_id("tab-myBooks")
        self.main_block = page.get_by_test_id("navigation__tabsList")
        self.favorite_button = self.main_block.get_by_test_id("icon_wishlist")
        self.drop_menu = self.page.get_by_role ("button", name = "Меню")
        self.remove_favorite_button = self.page.get_by_test_id("contextMenu__favorites--button")
        self.empty_state = self.page.get_by_test_id("empty-state-content")

    def clear_favorites_list(self):
        self.my_books_button.click()
        self.favorite_button.click(timeout=15000)
        while self.drop_menu.count() > 0:
            my_books_count_before = self.drop_menu.count()
            self.drop_menu.first.click(timeout=15000)
            self.remove_favorite_button.first.click(timeout=15000)
            expect(self.drop_menu).to_have_count(my_books_count_before - 1, timeout=15000)

        expect(self.empty_state).to_be_visible(timeout=15000)






