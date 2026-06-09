import pytest
from pathlib import Path

from fixtures.auth_fixture import *
from fixtures.cart_fixture import *
from fixtures.book_fixture import *
from fixtures.my_books_fixture import *

ROOT_DIR = Path(__file__).parent
AUTH_STATE_PATH = ROOT_DIR / "auth" / "litres_state.json"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": str(AUTH_STATE_PATH),
        "base_url": "https://www.litres.ru",
    }