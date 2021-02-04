from utilities.BaseClass import BaseClass


class CommonActions(BaseClass):

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def send_key_element(element,value):
        element.send_keys(value)