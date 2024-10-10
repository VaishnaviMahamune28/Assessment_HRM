from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddUserPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        
    NAV_PIM=(By.XPATH,"//span[text()='PIM']")
    Search_BAR_PIM=(By.XPATH,"(//input[@placeholder='Type for hints...'])[1]")
    search_btn=(By.CSS_SELECTOR, "input[type='submit']")
    ADD_BTN=(By.XPATH,"//button[text()=' Add ']")

    EMPLOYEE_FIRSTNAME_INPUT = (By.NAME, "firstName")
    EMPLOYEE_LASTNAME_INPUT = (By.NAME, "lastName")
    EMPLOYEE_ID=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")

    TOGGLE_BTN=(By.XPATH,"(//div[@class='oxd-switch-wrapper'])[1]")
    USRNAME=(By.XPATH,"(//input[@autocomplete='off'])[1]")
    PASS=(By.XPATH,"(//input[@type='password'])[1]")
    CON_PASS=(By.XPATH,"(//input[@type='password'])[2]")
    SAVE_DETAILS=(By.CSS_SELECTOR," button[type='submit']")
    


    def search_user_inPIM(self,userid):
        self.driver.find_element(*self.Search_BAR_PIM).send_keys(userid)
        self.driver.find_element(*self.search_btn).click()

    def Navigate_PIM(self):
        self.driver.find_element(*self.NAV_PIM).click()

    def add_user(self, employee_firstname, employe_lastname, emp_id):
        self.driver.find_element(*self.ADD_BTN).click()
        self.driver.find_element(*self.EMPLOYEE_FIRSTNAME_INPUT).send_keys(employee_firstname)
        self.driver.find_element(*self.EMPLOYEE_LASTNAME_INPUT).send_keys(employe_lastname)
        self.driver.find_element(*self.EMPLOYEE_ID).send_keys(emp_id)

    def toogle_on(self):
        self.wait.until(EC.element_to_be_clickable((self.TOGGLE_BTN))).click()

    def add_details(self,usrname):
        self.wait.until(EC.visibility_of_element_located((self.USRNAME))).send_keys(usrname)
        self.driver.find_element(*self.PASS).send_keys("Qwerty@123")
        self.driver.find_element(*self.CON_PASS).send_keys("Qwerty@123")
        self.driver.find_element(*self.SAVE_DETAILS).click()
        
        time.sleep(10)
