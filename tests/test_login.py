import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Navigate to the login page
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        # Initialize the LoginPage object
        self.login_page = LoginPage(self.driver)

        yield
        self.driver.quit()

    def test_valid_login(self):
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login_button()

        assert self.login_page.is_login_successful(), "Login failed with valid credentials"
