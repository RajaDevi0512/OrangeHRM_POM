'''
Login page contains all elements related to login page only.

This is a page object file
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from testData.Data import OrangeHRM_Data
from testLocator.locator import OrangeHRM_locator

class HRMLoginPage:
    driver = webdriver.Chrome()

    def start(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(OrangeHRM_Data.url)
        return True
    
    def login(self):
        self.driver.find_element(by= By.NAME, value=OrangeHRM_locator.userName_locator).send_keys(OrangeHRM_Data.userName)
        self.driver.find_element(by=By.NAME, value= OrangeHRM_locator.password_locator).send_keys(OrangeHRM_Data.password)
        self.driver.find_element(by=By.XPATH, value= OrangeHRM_locator.login_locator).click()
        return True
    
    def shutdown(self):
        self.driver.quit()
        return None