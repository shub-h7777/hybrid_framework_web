import pytest
from selenium import webdriver


class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demowebshop.tricentis.com/")
        yield
        self.driver.quit()
