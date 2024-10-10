import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.add_user_page import AddUserPage
from pages.user_management_page import UserManagementPage

class TestAPITesting:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        # Initialize the WebDriver (Selenium)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Navigate to the login page
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        # Initialize Page Objects
        self.login_page = LoginPage(self.driver)

        # Perform login before tests
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login_button()

        yield
        self.driver.quit()

    @pytest.fixture(scope="class")
    def get_users_response(self):
        """Fixture to get the API response for user details."""
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"
        response = requests.get(url)
        assert response.status_code == 200, "API call failed, expected status code 200."
        return response.json()


    '''Test to verify API status and response.'''
    def test_get_users_api(self, get_users_response):
        response_json = get_users_response
        assert "data" in response_json, "Response does not contain 'data'."


    """Test to validate the structure of the JSON response."""
    def test_structure_validation(self, get_users_response):
        response_json = get_users_response
        for user in response_json["data"]:
            assert "userName" in user, "User details do not contain 'userName'."
            assert "status" in user, "User details do not contain 'status'."
            assert "role" in user, "User details do not contain 'role'."
