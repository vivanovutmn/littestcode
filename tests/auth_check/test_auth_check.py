def test_auth_state_works(page):
    page.goto("/", wait_until="domcontentloaded")
    page.pause()