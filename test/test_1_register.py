import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestRegister(WebDriverWrapper):

    @pytest.mark.parametrize(
        "gender,firstname,lastname,email,password,registration_completed_message",
        data_source.test_valid_login_data
    )
    def test_valid_register(self, gender, firstname, lastname, email, password,registration_completed_message):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, f"gender-{gender}").click()
        self.driver.find_element(By.ID, "FirstName").send_keys(firstname)
        self.driver.find_element(By.ID, "LastName").send_keys(lastname)
        self.driver.find_element(By.ID, "Email").send_keys(email)
        self.driver.find_element(By.ID, "Password").send_keys(password)
        self.driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
        self.driver.find_element(By.ID, "register-button").click()
        registration_verification_message = self.driver.find_element(By.XPATH,
                                                                     "//div[contains(text(),'Your registration completed')]").text
        assert_that(registration_completed_message).is_equal_to(registration_verification_message)

    @pytest.mark.parametrize(
            "gender,firstname,lastname,email,password,email_validation",data_source.test_invalid_login_data)

    def test_invalid_register(self, gender, firstname, lastname, email, password,email_validation):   # we have already this {1}
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, f"gender-{gender}").click()
        self.driver.find_element(By.ID, "FirstName").send_keys(firstname)
        self.driver.find_element(By.ID, "LastName").send_keys(lastname)
        self.driver.find_element(By.ID, "Email").send_keys(email)
        self.driver.find_element(By.ID, "Password").send_keys(password)
        self.driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
        self.driver.find_element(By.ID, "register-button").click()
        email_validation_message=self.driver.find_element(By.XPATH,"//span[text()='Wrong email']").text
        assert_that(email_validation_message).is_equal_to(email_validation)
