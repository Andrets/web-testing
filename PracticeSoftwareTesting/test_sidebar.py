import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helpers as hp
import PracticeSoftwareTesting.helpers as th
from PracticeSoftwareTesting.web_config import WebAuthorization


class SidebarTest(unittest.TestCase):
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

    def test_02_sidebar_test(self):
        driver = self.driver
        time.sleep(hp.time_max)
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, hp.time_wait)

        try:
            # Click to top menu home btn
            driver.find_element(By.XPATH, hp.top_menu_home).click()

            # First card in list
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.first_card_main_page))
            )
            driver.find_element(By.XPATH, hp.first_card_main_page).click()

            # Get product name
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
            product_name_locator = driver.find_element(By.XPATH, "//h1")
            product_name = product_name_locator.text.strip()
            print(f"Product name is: {product_name}")

            # Get category name
            category_name_locator = driver.find_element(
                By.XPATH, "//span[@aria-label='category']"
            )
            category_name = category_name_locator.text.strip()
            print(f"Product name is: {category_name}")

            # Get brand
            brand_name_locator = driver.find_element(
                By.XPATH, "//span[@aria-label='brand']"
            )
            brand_name = brand_name_locator.text.strip()
            print(f"Product name is: {brand_name}")

            # Get product price
            price_locator = driver.find_element(
                By.XPATH, "//span[@aria-label='unit-price']"
            )
            price = float(price_locator.text)
            print(f"Product price is: {price}")

            # Go back to home page
            driver.back()
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.sort_select_main_page))
            )

            # Sort - Choose Price (High - Low)
            driver.find_element(By.XPATH, hp.sort_select_main_page).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.select_sort_main_page)))
            driver.find_element(By.XPATH, hp.select_sort_main_page).click()

            # Counting the necessary values
            target_min = max(0, int(price) - 1)
            target_max = int(price) + 1
            print(f"Ставим диапазон: {target_min} - {target_max}")

            # Finding the sliders
            slider_min = driver.find_element(
                By.XPATH, "//span[contains(@class, 'pointer-min')]"
            )
            slider_max = driver.find_element(
                By.XPATH, "//span[contains(@class, 'pointer-max')]"
            )

            # Getting the current values of the sliders
            current_min = int(slider_min.get_attribute("aria-valuenow"))
            current_max = int(slider_max.get_attribute("aria-valuenow"))

            # Move the minimum slider to target_min
            diff_min = target_min - current_min
            for _ in range(abs(diff_min)):
                if diff_min > 0:
                    slider_min.send_keys(Keys.ARROW_RIGHT)
                else:
                    slider_min.send_keys(Keys.ARROW_LEFT)

            # Move the maximum slider to target_max
            diff_max = current_max - target_max
            for _ in range(abs(diff_max)):
                if diff_max > 0:
                    slider_max.send_keys(Keys.ARROW_LEFT)
                else:
                    slider_max.send_keys(Keys.ARROW_RIGHT)

            # Enter the product name in the search field
            driver.find_element(By.XPATH, hp.search_main_page).send_keys(product_name)
            time.sleep(hp.time_mid)
            # Click to Search btn
            driver.find_element(By.XPATH, hp.search_btn_main_page).click()
            time.sleep(hp.time_max)

            # In the Category checkboxes, select the appropriate one
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.checkbox_category_main_page)
                )
            )
            category_element = driver.find_element(
                By.XPATH, f"//label[normalize-space()='{category_name}']"
            )
            driver.execute_script("arguments[0].scrollIntoView()", category_element)
            driver.find_element(
                By.XPATH, f"//label[normalize-space()='{category_name}']"
            ).click()
            time.sleep(hp.time_max)

            # In the Brand checkboxes, select the appropriate one
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.checkbox_brand_main_page)
                )
            )
            brand_element = driver.find_element(
                By.XPATH, f"//label[normalize-space()='{category_name}']"
            )
            driver.execute_script("arguments[0].scrollIntoView()", brand_element)
            driver.find_element(
                By.XPATH, f"//label[normalize-space()='{brand_name}']"
            ).click()
            time.sleep(hp.time_max)

            # Check the data of the selected product
            # Make sure there is only one card on the page
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@class='card']"))
            )
            cards = driver.find_elements(By.XPATH, "//a[@class='card']")
            assert len(cards) == 1, f"Expected 1 card, but found: {len(cards)}"

            # Check valid product name
            product_name_main_page_locator = driver.find_element(By.XPATH, "//h5")
            actual_text = product_name_main_page_locator.text.strip()
            expected_text = product_name
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # Check valid product price
            price_main_page_locator = driver.find_element(
                By.XPATH, "//span[@data-test='product-price']"
            )
            card_price = price_main_page_locator.text.strip()
            actual_text = float(card_price.replace("$", ""))
            expected_text = price
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

        except Exception as e:
            th.take_screenshot(driver, name=f"sidebar_error_{self.browser_name}")
            self.fail(f"The test failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
