from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.name = (By.ID, ":r0:-form-item")
        self.email = (By.ID, ":r1:-form-item")
        self.password = (By.ID, ":r2:-form-item")
        self.confirm_password = (By.ID, ":r3:-form-item")
        self.register_button = (By.XPATH, "//button[normalize-space()='Register']")
        # Update this after inspecting your page source!
        self.flash_message = (
            By.XPATH,
            "//div[contains(text(),'Failed to fetch')]",
        )

    def load(self):
        self.driver.get("https://v2.hairnerds.id/register")

    def register(self, name, email, password, confirm_password):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)
        self.driver.find_element(*self.register_button).click()


    def get_flash_message(self):
        print(self.driver.page_source)  # Add this line
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.flash_message))
        return element.text
