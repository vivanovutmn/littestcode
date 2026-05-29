from playwright.sync_api import Page, TimeoutError, expect
from test_data import TestUser, TestBook


class LoginPage:


    def __init__(self, page: Page):
        self.page = page
        self.login = page.get_by_test_id("tab-login").get_by_test_id("tab__link")
        self.login_input = self.page.get_by_test_id("auth__input--enterEmailOrLogin")
        self.login_button = self.page.get_by_test_id("auth__button--continue")
        self.password_input = self.page.get_by_test_id("auth__input--enterPassword")
        self.password_button = self.page.get_by_test_id("auth__button--enter")
        self.cookie_button = self.page.get_by_test_id("cookieAcceptPopup__accept")

    def do_login (self):
        self.login.click()
        self.login_input.fill(TestUser.login)
        self.login_button.click()
        self.password_input.fill(TestUser.password)
        self.password_button.click()
        try:
            self.cookie_button.click(timeout=3000)
        except TimeoutError:
            pass


class SearchPage:

    def __init__(self, page: Page):
        self.page = page
        self.search_input = self.page.get_by_test_id("search__input")

    def search_book (self, book_name: str):
        self.search_input.fill(book_name)
        self.search_input.press("Enter")


    def open_book (self, book_card_name: str):
        book_card = self.page.get_by_role("group", name=book_card_name)
        with self.page.expect_popup() as popup_info:
            book_card.get_by_test_id ("art__cover").click()

        book_page = popup_info.value
        book_page.wait_for_load_state()
        return book_page

class BookPage:


    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart = page.get_by_test_id("book__addToCartButton")
        self.add_close = page.get_by_role ("button", name="Закрыть")
        self.cart = page.get_by_test_id("book__goToCartButton")
        self.cookie_button = self.page.get_by_test_id("cookieAcceptPopup__accept")

        self.review_wrapper = page.get_by_test_id("comment-system__AddReview--wrapper")
        self.five_stars = self.review_wrapper.get_by_test_id("bookRating__stars--5")
        self.review_textarea = page.get_by_test_id("comment--textArea")
        self.publish_review_button = page.get_by_test_id("public__review--button")
        self.edit_review_button = page.get_by_test_id("edit__review--button")

    def add_book (self):
        try:
            self.cookie_button.click(timeout=3000)
        except TimeoutError:
            pass
        self.add_to_cart.click()
        self.add_close.click()
        self.cart.click()

    def set_five_star_rating(self):
        self.five_stars.click()

    def publish_review(self, review_text: str):
        self.set_five_star_rating()
        self.review_textarea.fill(review_text)
        self.publish_review_button.click()

        expect(self.page.get_by_text(review_text)).to_be_visible(timeout=15000)

    def edit_review(self, review_text: str):
        expect(self.edit_review_button).to_be_visible(timeout=15000)
        self.edit_review_button.click()

        self.review_textarea.fill(review_text)
        self.publish_review_button.click()

        expect(self.page.get_by_text(review_text)).to_be_visible(timeout=15000)

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        #self.delete_book = page.get_by_test_id(f"cart__listItem--{TestBook.book_test_id}").get_by_test_id("cart__listDeleteButton")
        self.confirm_delete = self.page.get_by_test_id("cart__modalDeleteArt--button-primary")
        self.happy_path=page.get_by_test_id("empty-state-content")
    def delete_book_by_name(self, book_card_name: str):
        cart_item = self.page.locator('[data-testid^="cart__listItem"]').filter(has_text=TestBook.cart_title)
        expect(cart_item).to_be_visible()
        delete_book = cart_item.get_by_test_id("cart__listDeleteButton")
        delete_book.click()
        self.confirm_delete.click()
    # def del_book (self):
    #     self.delete_book.click()
    #     self.confirm_delete.click()
