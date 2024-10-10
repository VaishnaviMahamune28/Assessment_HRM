import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.add_user_page import AddUserPage
from pages.user_management_page import UserManagementPage


class TestAddUser:
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
        self.add_user_page = AddUserPage(self.driver)

        # Perform login before tests
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login_button()

        yield
        self.driver.quit()


    def test_add_user(self):
        self.add_user_page.Navigate_PIM()
        try:
            self.add_user_page.search_user_inPIM('Amelia')
        except:
            self.add_user_page.add_user(employee_firstname='amph', employe_lastname='phil', emp_id='989060')
            self.add_user_page.toogle_on()
            self.add_user_page.add_details("amphphil")


        user_id_logo = self.driver.find_element(By.CLASS_NAME, 'employee-image')
        assert user_id_logo.is_displayed(), "User ID logo is not displayed"