import pytest
from playwright.async_api import async_playwright, Page, expect

@pytest.fixture()
def start_page (page: Page):
    page.goto("http://litres.ru", wait_until="domcontentloaded")

    return page
