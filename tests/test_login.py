from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Tom", "SuperSecretPassword!")

    # message = login_page.get_flash_message()
    # assert "You logged in successfully!" in message
