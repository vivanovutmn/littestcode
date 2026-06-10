# from playwright.sync_api import Page, expect
#
#
# class BookPage:
#
#     def __init__(self, page: Page):
#         self.page = page
#
#         # Видимый desktop-блок покупки/действий книги
#         self.book_sale_block = page.get_by_test_id("book-sale-block__wrapper")
#         self.fav_button = self.book_sale_block.locator(
#             '[data-analytics-id="wishlist-button"]'
#         )
#
#         self.add_to_cart = page.get_by_test_id("book__addToCartButton")
#         self.add_close = page.get_by_role("button", name="Закрыть")
#         self.cart = page.get_by_test_id("book__goToCartButton")
#         self.cookie_button = page.get_by_test_id("cookieAcceptPopup__accept")
#
#         self.review_wrapper = page.get_by_test_id("comment-system__AddReview--wrapper")
#         self.five_stars = self.review_wrapper.get_by_test_id("bookRating__stars--5")
#         self.review_textarea = page.get_by_test_id("comment--textArea")
#         self.publish_review_button = page.get_by_test_id("public__review--button")
#         self.edit_review_button = page.get_by_test_id("edit__review--button")
#
#         self.finish_button = page.get_by_test_id("modal__finishButton")
#         self.unfinish_button = page.get_by_test_id("modal__finishButton--finished")
#
#     def add_to_favorites(self):
#         expect(self.book_sale_block).to_be_visible(timeout=15000)
#         expect(self.fav_button).to_be_visible(timeout=15000)
#
#         self.fav_button.click()
#
#         expect(
#             self.fav_button.get_by_test_id("icon_favoritesFilled")
#         ).to_be_visible(timeout=15000)
#
#     def remove_from_favorites(self):
#         expect(self.book_sale_block).to_be_visible(timeout=15000)
#         expect(self.fav_button).to_be_visible(timeout=15000)
#
#         self.fav_button.click()
#
#         expect(
#             self.fav_button.get_by_test_id("icon_favorites")
#         ).to_be_visible(timeout=15000)
#
#     def should_be_in_favorites(self):
#         expect(
#             self.fav_button.get_by_test_id("icon_favoritesFilled")
#         ).to_be_visible(timeout=15000)
#
#     def should_not_be_in_favorites(self):
#         expect(
#             self.fav_button.get_by_test_id("icon_favorites")
#         ).to_be_visible(timeout=15000)
#
#     def finish_book(self):
#         expect(self.finish_button).to_be_visible(timeout=15000)
#
#         self.finish_button.click()
#
#         expect(self.unfinish_button).to_be_visible(timeout=15000)
#
#     def unfinish_book(self):
#         expect(self.unfinish_button).to_be_visible(timeout=15000)
#
#         self.unfinish_button.click()
#
#         expect(self.finish_button).to_be_visible(timeout=15000)

from playwright.sync_api import Page, expect


class BookPage:

    def __init__(self, page: Page):
        self.page = page

        self.book_sale_block = page.get_by_test_id("book-sale-block__wrapper")
        self.fav_button = self.book_sale_block.locator(
            '[data-analytics-id="wishlist-button"]'
        )

        self.add_to_cart = page.get_by_test_id("book__addToCartButton")
        self.add_close = page.get_by_role("button", name="Закрыть")
        self.cart = page.get_by_test_id("book__goToCartButton")
        self.cookie_button = page.get_by_test_id("cookieAcceptPopup__accept")

        self.review_wrapper = page.get_by_test_id("comment-system__AddReview--wrapper")
        self.five_stars = self.review_wrapper.get_by_test_id("bookRating__stars--5")
        self.review_textarea = page.get_by_test_id("comment--textArea")
        self.publish_review_button = page.get_by_test_id("public__review--button")
        self.edit_review_button = page.get_by_test_id("edit__review--button")

        self.finish_button = page.get_by_test_id("modal__finishButton")
        self.unfinish_button = page.get_by_test_id("modal__finishButton--finished")

    def empty_favorite_icon(self):
        return self.fav_button.get_by_test_id("icon_favorites")

    def filled_favorite_icon(self):
        return self.fav_button.get_by_test_id("icon_favoritesFilled")

    def add_to_favorites(self):
        expect(self.book_sale_block).to_be_visible(timeout=20000)
        expect(self.fav_button).to_be_visible(timeout=20000)

        if self.filled_favorite_icon().count() > 0:
            return

        self.fav_button.click()

        self.page.reload(wait_until="domcontentloaded")

        expect(self.filled_favorite_icon()).to_be_attached(timeout=20000)
        expect(self.empty_favorite_icon()).to_have_count(0, timeout=20000)

    def remove_from_favorites(self):
        expect(self.book_sale_block).to_be_visible(timeout=20000)
        expect(self.fav_button).to_be_visible(timeout=30000)

        if self.empty_favorite_icon().count() > 0:
            return

        self.fav_button.click()

        self.page.reload(wait_until="domcontentloaded")

        expect(self.empty_favorite_icon()).to_be_attached(timeout=20000)
        expect(self.filled_favorite_icon()).to_have_count(0, timeout=20000)

    def should_be_in_favorites(self):
        expect(self.filled_favorite_icon()).to_be_attached(timeout=15000)
        expect(self.empty_favorite_icon()).to_have_count(0, timeout=15000)

    def should_not_be_in_favorites(self):
        expect(self.empty_favorite_icon()).to_be_attached(timeout=15000)
        expect(self.filled_favorite_icon()).to_have_count(0, timeout=15000)

    def finish_book(self):
        expect(self.finish_button).to_be_visible(timeout=15000)
        self.finish_button.click()
        expect(self.unfinish_button).to_be_visible(timeout=15000)

        self.page.reload(wait_until="domcontentloaded")

    def unfinish_book(self):
        expect(self.unfinish_button).to_be_visible(timeout=15000)
        self.unfinish_button.click()
        expect(self.finish_button).to_be_visible(timeout=15000)

        self.page.reload(wait_until="domcontentloaded")