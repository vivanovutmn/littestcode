import allure


@allure.feature("Прочитанное")
@allure.story("Добавление и удаление книги")
@allure.title("Пользователь может добавить книгу в прочитанное и удалить её")
def test_add_and_remove_book_from_favorites(book_unread):
    with allure.step ("Добавление в почитанное"):
        book_unread.finish_book()
    with allure.step("Удаление из прочитанного"):
        book_unread.unfinish_book()