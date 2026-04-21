import os
import random
import string
import time
import unittest

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helpers as hp
import PracticeSoftwareTesting.helpers as th
from PracticeSoftwareTesting.web_config import WebAuthorization


class BuyProductToCardTest(unittest.TestCase):
    driver: webdriver.Remote
    browser_name: str

    @classmethod
    def setUpClass(cls):
        browser = os.environ.get("BROWSER", "chrome").lower()
        cls.browser_name = browser
        if browser not in th.DRIVERS:
            raise ValueError(f"Unsupported browser: {browser}")
        cls.driver = th.DRIVERS[browser]()
        cls.driver.maximize_window()
        allure.dynamic.parameter("browser", browser)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_authorization(self):
        try:
            web_authorization = WebAuthorization(self.driver)
            web_authorization.test_web_authorization()
        except AssertionError as e:
            print(e)
            self.fail("The test failed: an authorization issue")

    def test_02_byu_product(self):
        driver = self.driver
        time.sleep(hp.time_max)
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, hp.time_wait)

        try:
            # Click to Category on top menu
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.top_menu_category))
            )
            driver.find_element(By.XPATH, hp.top_menu_category).click()
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.subcategory_handing_tools)
                )
            )
            driver.find_element(By.XPATH, hp.subcategory_handing_tools).click()

            # Wait first card on list
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.first_card_main_page))
            )
            driver.find_element(By.XPATH, hp.first_card_main_page).click()
            time.sleep(hp.time_mid)

            # Get product name
            product_name_locator = driver.find_element(By.XPATH, "//h1")
            product_name = product_name_locator.text.strip()
            print(f"Product name is: {product_name}")

            # Get product price
            price_locator = driver.find_element(
                By.XPATH, "//span[@aria-label='unit-price']"
            )
            price = float(price_locator.text)
            print(f"Product price is: {price}")

            # Press the button 10 times +
            btn_more = driver.find_element(By.XPATH, hp.btn_more_product_page)
            for i in range(10):
                btn_more.click()
                time.sleep(hp.time_min)

            # Click "Add to cart"
            driver.find_element(By.XPATH, hp.add_to_cart_product_page).click()
            time.sleep(hp.time_mid)

            # Click to top menu cart icon
            driver.find_element(By.XPATH, hp.top_menu_cart_shopping).click()
            time.sleep(hp.time_mid)

            # CART
            # Click to Proceed to checkout
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.btn_proceed_to_checkout))
            )
            driver.find_element(By.XPATH, hp.btn_proceed_to_checkout).click()
            time.sleep(hp.time_mid)

            # SIGHN IN
            # Check text Hello Jhon Doe ......
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.text_hello_admin_product_page)
                )
            )

            # Click to Proceed to checkout
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.btn_proceed_to_checkout_2)
                )
            )
            driver.find_element(By.XPATH, hp.btn_proceed_to_checkout_2).click()
            time.sleep(hp.time_mid)

            # BILLING ADDRESS
            # Clearing the Street City, State, Country, Postal code input field and Entering new data
            fields_data = {
                hp.input_field_street_cart_page: "123 Main Street",
                hp.input_field_city_cart_page: "New York",
                hp.input_field_state_cart_page: "NY",
                hp.input_field_country_cart_page: "USA",
                hp.input_field_postal_code_cart_page: "10001",
            }

            for xpath, value in fields_data.items():
                field = self.driver.find_element(By.XPATH, xpath)
                field.send_keys(Keys.CONTROL + "a")
                field.send_keys(Keys.BACKSPACE)
                field.send_keys(value)

            # Click to Proceed to checkout btn
            driver.find_element(By.XPATH, hp.btn_proceed_to_checkout_3).click()
            time.sleep(hp.time_mid)

            # PAYMENT
            # title
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.payment_title_cart_page))
            )

            # Click to select
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.select_payment_method)))
            driver.find_element(By.XPATH, hp.select_payment_method).click()
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.select_cash_to_delivery_cart_page)
                )
            )
            driver.find_element(By.XPATH, hp.select_cash_to_delivery_cart_page).click()
            time.sleep(hp.time_mid)

            # Click to Cpnfirm
            driver.find_element(By.XPATH, hp.btn_confirm_cart_page).click()
            time.sleep(hp.time_mid)

            # Check success notification
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.success_notification_cart_page)
                )
            )

        except Exception as e:
            th.take_screenshot(
                driver, name=f"buy_product_to_card_error_{self.browser_name}"
            )
            self.fail(f"The test failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
