from utils.element_locator import ElementLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class StarAtlasPage:
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def get_driver(cls):
        return WebDriver.get_driver()

    def login(self, username, password):
        username_locator = ElementLocator.get_locator("username_input")
        password_locator = ElementLocator.get_locator("password_input")
        login_button_locator = ElementLocator.get_locator("login_button")

        self.driver.find_element(username_locator[0], username_locator[1]).send_keys(username)
        self.driver.find_element(password_locator[0], password_locator[1]).send_keys(password)
        self.driver.find_element(login_button_locator[0], login_button_locator[1]).click()
        time.sleep(5)  # Add proper waits

    def is_profile_visible(self):
        return "Your Profile" in self.driver.page_source

    def click_element(self, element_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(element_locator))
        self.driver.find_element(element_locator[0], element_locator[1]).click()

    def is_page_visible(self, page):
        return page.lower() in self.driver.current_url.lower()
