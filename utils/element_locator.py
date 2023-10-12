import json
from selenium.webdriver.common.by import By


class ElementLocator:
    @classmethod
    def get_locator(cls, element_name):
        with open('utils/element_config.json') as config_file:
            element_config = json.load(config_file)
            element = element_config[element_name]

        locator_type = element["locator_type"]
        locator_value = element["locator_value"]
        return cls.get_locator_type(locator_type), locator_value

    @staticmethod
    def get_locator_type(locator_type):
        if locator_type.lower() == 'id':
            return By.ID
        elif locator_type.lower() == 'name':
            return By.NAME
        elif locator_type.lower() == 'xpath':
            return By.XPATH
