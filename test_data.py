import os
from dotenv import load_dotenv
load_dotenv()
class TestUser:
    login = os.getenv("LITRES_LOGIN")
    password = os.getenv("LITRES_PASSWORD")
class TestBook:
    search_text ="Ведьмак"
    card_name = "Ведьмак в озвучке Всеволода Кузнецова"
    book_test_id = 70548067