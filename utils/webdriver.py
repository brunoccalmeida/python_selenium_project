from selenium import webdriver


class WebDriver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            cls._driver = webdriver.Chrome(options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
