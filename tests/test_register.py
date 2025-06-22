from pages.register_page import RegisterPage

def test_valid_register(driver):
    register_page = RegisterPage(driver)
    register_page.load()
    register_page.register("Tom", "tom@mailinator.com", "SuperSecretPassword!", "SuperSecretPassword!")

    # message = register_page.get_flash_message()
    # assert "You registered successfully!" in message
