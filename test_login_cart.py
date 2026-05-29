from playwright.sync_api import expect
from login_cart_page import LoginPage, SearchPage, BookPage, CartPage

def test_add_del_book (start_page):
    login_page = LoginPage (start_page)
    login_page.do_login()

    search_page = SearchPage (start_page)
    search_page.search_book("Ведьмак")

    book_page = search_page.open_book ("Ведьмак в озвучке Всеволода Кузнецова. Анджей Сапковский. Аудио. Хит продаж")
    book_page_object = BookPage (book_page)
    book_page_object.add_book()

    cart_page = CartPage (book_page)
    cart_page.del_book()
    expect(cart_page.happy_path).to_be_visible()





