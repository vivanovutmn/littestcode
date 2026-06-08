from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.confirm_delete = self.page.get_by_test_id("cart__modalDeleteArt--button-primary")
        self.happy_path=page.get_by_test_id("empty-state-content")
    def delete_book_by_name(self, cart_title):
        cart_item = self.page.locator('[data-testid^="cart__listItem"]').filter(has_text=cart_title)
        expect(cart_item).to_be_visible(timeout=15000)
        delete_book = cart_item.get_by_test_id("cart__listDeleteButton")
        delete_book.click()
        self.confirm_delete.click()
        expect(cart_item).to_be_hidden(timeout=10000)