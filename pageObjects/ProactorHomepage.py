from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


class ProactorHomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    "//input[@class='form-control ng-pristine ng-invalid ng-touched']"
    name = (By.XPATH, "//input[@class='form-control ng-pristine ng-invalid ng-touched1']")
    email = (By.XPATH, "//input[@name='email1']")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    submit = (By.XPATH, "//input[@class='btn btn-success']")

    @step("In get name Proactor Homepage")
    def getName(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,"//input[@class='form-control ng-pristine ng-invalid ng-touched']")))
            return element
        except:
            self.getLogger().error("Unable to get  name field in Proactor Homepage")
            raise


    @step("In get email Proactor Homepage")
    def getEmail(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.email))
            return element
        except:
            self.getLogger().error("Unable to get email field in Proactor Homepage")
            raise
    @step("In get password Proactor Homepage")
    def getPassword(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.password))
            return element
        except:
            self.getLogger().error("Unable to get password field in Proactor Homepage")
            raise
    @step("In get submit Proactor Homepage")
    def getSubmit(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.submit))
            return element
        except:

            self.getLogger().error("Unable to click submit button in Proactor Homepage")
            raise