from playwright.sync_api import sync_playwright

def test_playwright():
    print('Testando o playwright...')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://analista-teste.seatecnologia.com.br/")
        print(page.title())
        browser.close()
