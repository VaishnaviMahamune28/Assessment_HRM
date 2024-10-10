import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

class TestUserSearch:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Navigate to the login page
        self.driver.get("https://opensource-demo.orangehrmlive.com ")

        # Initialize Page Objects
        self.login_page = LoginPage(self.driver)
        self.user_management_page = UserManagementPage(self.driver)

        # Perform login before tests
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login_button()

        yield
        self.driver.quit()

    def test_search_user(self):
        # Search for a user and verify search results
        self.user_management_page.Navigate_admin()
        self.user_management_page.search_for_user("Admin")
        self.user_management_page.click_search_option()
        assert self.user_management_page.is_search_result_displayed(), "Search results are not displayed"

        # Open user details page and validate navigation
        #self.user_management_page.open_user_details()
        #assert "userDetails" in self.driver.current_url, "Failed to navigate to user details page"
