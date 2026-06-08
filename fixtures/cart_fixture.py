import pytest
from playwright.sync_api import Page, expect

@pytest.fixture()
def authorized_empty_cart_page (authorized_page: Page):
    clear_the_cart(authorized_page)
    yield authorized_page
    clear_the_cart(authorized_page)


def clear_the_cart(page: Page):
    page.goto("/my-books/cart/", wait_until="domcontentloaded")

    cart_items = page.locator('[data-testid^="cart__listItem--"]')
    confirm_delete = page.get_by_test_id("cart__modalDeleteArt--button-primary")
    empty_cart = page.get_by_test_id("empty-state-content")

    expect(
        cart_items.first.or_(empty_cart)
    ).to_be_visible(timeout=15000)

    while cart_items.count() > 0:
        count_before = cart_items.count()

        cart_items.first.get_by_test_id("cart__listDeleteButton").click()
        confirm_delete.click()

        expect(cart_items).to_have_count(count_before - 1, timeout=10000)