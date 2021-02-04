from allure_commons.types import AttachmentType

from utilities.BaseClass import BaseClass
import  allure
import pytest
from TestData.GetData import getdata


class TestPractice(BaseClass):
    @allure.story('epic_1')  # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case

    def test_e2e(self,getData):
        log = self.getLogger()
        log.info("getting all the card titles")
        allure.step(getData["firstname"])
        print(getData)
        self.driver.get("https://stackoverflow.com/questions/50387694/in-my-pom-structure-i-get-error-modulenotfounderror-no-module-named-pages")
        #allure.attach(self.driver.get_screenshot_as_png(), name="link screen", attachment_type=AttachmentType.png)
        #assert getData["firstname"] == 'Example Domains'
        log.info("Entering country name as ind")
        log.info("Text received from application is ")
        #assert ("Success")

    @pytest.fixture(params=getdata.getdatafromexcel("C:\\Users\\91998\\Desktop\\Python Demo.xlsx", "Sheet1"))
    def getData(self, request):
        return request.param

