from playwright.sync_api import sync_playwright

AUTH_STATE_PATH = "auth/litres_state.json"

def main ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.litres.ru/", wait_until="domcontentloaded")
        print ("Авторизуйся вручную: логин/почта, пароль/код из письма")
        print ("Когда будешь уверен, что авторизован вернись в терминал и нажми Enter")
        input()

        context.storage_state(path=AUTH_STATE_PATH)

        print(f"Storage state сохранен в {AUTH_STATE_PATH}")
        browser.close()
if __name__ == "__main__":
    main()