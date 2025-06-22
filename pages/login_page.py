from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, ":r0:-form-item")
        self.password_input = (By.ID, ":r1:-form-item")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")
        self.flash_message = (By.XPATH, "//div[contains(text(),'Failed to fetch')]")

    def load(self):
        self.driver.get("https://v2.hairnerds.id/login")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


    def get_flash_message(self):
        print(self.driver.page_source)  # Add this line
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.flash_message))
        return element.text
