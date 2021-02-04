import pytest
from allure_commons.types import AttachmentType

from pageObjects.ProactorHomepage import ProactorHomePage
from utilities.BaseClass import BaseClass
import allure
from TestData.GetData import getdata


class TestProactorHomePage(BaseClass):

    def test_formSubmission(self,getData):
        try:
            log = self.getLogger()
            self.driver.get("https://rahulshettyacademy.com/angularpractice/")
            home_page = ProactorHomePage(self.driver)
            log.info("first name is " + getData["Name"])
            # home_page.getName().send_keys(getData["Name"])
            allure.step("name Entered")
            home_page.getEmail().send_keys(getData["Email"])
            allure.step("email Entered")
            home_page.getPassword().send_keys(getData["Password"])
            allure.step("password Entered")
            home_page.getSubmit().click()
            allure.step("Submit button clicked")
            allure.attach(self.driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
            self.driver.refresh()
        except:
            self.getLogger().error("Unable to run test form submission")
            allure.attach(self.driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)

            self.assertEqual("h", "p", "h is not equal to p")
    @pytest.fixture(params=getdata.getdatafromexcel("C:\\Users\\91998\\Desktop\\Python Demo.xlsx","Sheet2"))
    def getData(self, request):
        return request.param
