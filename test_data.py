import os
from dotenv import load_dotenv
load_dotenv()
class TestUser:
    # login = os.getenv("LITRES_LOGIN")
    # password = os.getenv("LITRES_PASSWORD")
    login = 'dr.vladimir0318@gmail.com'
    password = 'Qwerty123'
class TestBook:
    search_text ="Ведьмак"
    card_name = "Меч Предназначения. Анджей Сапковский. Текст, доступен аудиоформат"
    book_test_id = 70548067
    cart_title = "Меч Предназначения"
    cart_author = "Анджей Сапковский"
    cart_format = "Текст"

class TestReview:
    initial_text = "Моя любимая книга серии, слушал в озвучке Всеволода Кузнецова"
    edited_text = "Моя любимая книга серии, слушать нужно обязательно в озвучке Всеволода Кузнецова"