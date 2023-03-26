import time

import pytest
from assertpy import assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import test_data
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestShoppingCart(WebDriverWrapper):

    @pytest.mark.parametrize("email,password"
        ,data_source.test_case_3_data
                             )
    def test_add_books(self, email, password):
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "Email").send_keys(email)
        self.driver.find_element(By.ID, "Password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        # verify Account Enail is same which we used during login
        account_email = self.driver.find_element(By.LINK_TEXT, email).text
        assert_that(account_email).is_equal_to(email)

        # Verify Shopping cart as 0 and hover over it and verify the TEXT on Hovering.
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//span[text()='Shopping cart']")).perform()
        shopping_cart_null_text = self.driver.find_element(By.XPATH,
                                                           "//div[contains(text(),'You have no items in your shopping cart.')]").text
        assert_that(shopping_cart_null_text).is_equal_to("You have no items in your shopping cart.")

        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Books'])[3]").click()
        self.driver.find_element(By.XPATH, "//input[@value='Add to cart']").click()
        action.move_to_element(self.driver.find_element(By.XPATH, "//span[text()='Shopping cart']")).perform()
        add_to_cart_confirmation = self.driver.find_element(By.XPATH, "//p[@class='content']").text
        assert_that(add_to_cart_confirmation).is_equal_to("The product has been added to your shopping cart")

        # log out and verify login is displayed
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.find_element(By.LINK_TEXT, "Log in").is_displayed()

        # HOW TO VERIFY THE BEFORE AND AFTER TEXT OF THE SHOPPING CART(0)

        # shopping_cart_not_null_text=self.driver.find_element(By.XPATH,"//div[@class='count']").get_attribute("value")
        # print(shopping_cart_not_null_text)
        # assert_that().is_not_equal_to(shopping_cart_null_text)

        time.sleep(5)

    @pytest.mark.parametrize("email,password"
        , data_source.test_case_3_data
                             )
    def test_books_are_in_shopping_cart_after_relogin(self,email,password):
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "Email").send_keys(email)
        self.driver.find_element(By.ID, "Password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        # verify Account Enail is same which we used during login
        account_email = self.driver.find_element(By.LINK_TEXT, email).text
        assert_that(account_email).is_equal_to(email)

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//span[text()='Shopping cart']")).perform()
        book_name = self.driver.find_element(By.XPATH, "//div/a[text()='Computing and Internet']").text
        assert_that("Computing and Internet").is_equal_to(book_name)
        book_price = self.driver.find_element(By.XPATH, "//div[@class='price']/span").text
        print(book_price)
        sub_total = self.driver.find_element(By.XPATH, "//div[@class='totals']/strong").text
        print(sub_total)
        self.driver.find_element(By.XPATH, "//input[@value='Go to cart']").click()

        # after clicking on go to cart verify the price, subtotal and book name
        assert_that(book_name).is_equal_to(self.driver.find_element(By.XPATH, "//a[@class='product-name']").text)
        assert_that(book_price).is_equal_to(
            self.driver.find_element(By.XPATH, "//span[@class='product-unit-price']").text)
        assert_that(sub_total).is_equal_to(self.driver.find_element(By.XPATH, "//span[@class='product-price']").text)

        # remove the book from cart
        self.driver.find_element(By.NAME, "removefromcart").click()
        self.driver.find_element(By.NAME, "updatecart").click()

        action.move_to_element(self.driver.find_element(By.XPATH, "//span[text()='Shopping cart']")).perform()
        shopping_cart_null_text = self.driver.find_element(By.XPATH,
                                                           "//div[contains(text(),'You have no items in your shopping cart.')]").text
        assert_that(shopping_cart_null_text).is_equal_to("You have no items in your shopping cart.")

        # log out and verify login is displayed
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.driver.find_element(By.LINK_TEXT, "Log in").is_displayed()
