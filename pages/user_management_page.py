from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserManagementPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        

    SEARCH_BAR = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    SEARCH_CLICK=(By.CSS_SELECTOR,"button[type='submit']")
    SEARCH_RESULTS = (By.XPATH, "(//div[contains(text(),'Admin')])[1]")
    Nav_admin=(By.XPATH,"//li[1]//a[1]//span[1]")
    
    #USER_LINK = (By.XPATH, "//a[text()='Bhuvaneshwar']")

    

    def Navigate_admin(self):
        self.wait.until(EC.element_to_be_clickable((self.Nav_admin))).click()

    def search_for_user(self, username: str):
        self.driver.find_element(*self.SEARCH_BAR).send_keys(username)

    def click_search_option(self):
        self.driver.find_element(*self.SEARCH_CLICK).click()

    def is_search_result_displayed(self) -> bool:
        return len(self.driver.find_elements(*self.SEARCH_RESULTS)) > 0
    
    

    

  #  def open_user_details(self):
        #self.driver.find_element(*self.USER_LINK).click()
