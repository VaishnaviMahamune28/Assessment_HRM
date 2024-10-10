from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    # Define locators for elements on the login page
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login ']")
    USER_SPECIFIC_ELEMENT = (By.ID, "app")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Method to enter username
    def enter_username(self, username: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    # Method to enter password
    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    # Method to click the login button
    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Method to check if login was successful
    def is_login_successful(self) -> bool:
        try:
            return self.driver.find_element(*self.USER_SPECIFIC_ELEMENT).is_displayed()
        except:
            return False
