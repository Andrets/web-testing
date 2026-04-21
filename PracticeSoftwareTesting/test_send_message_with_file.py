import os
import time
import unittest

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helpers as hp
import PracticeSoftwareTesting.helpers as th


class SendMessageWithTextTest(unittest.TestCase):
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

    def setUp(self):
        allure.dynamic.parameter("browser", self.browser_name)

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    def test_01_registration(self):
        driver = self.driver
        driver.get(hp.url)
        time.sleep(hp.time_max)
        actions = webdriver.ActionChains(driver)
        wait = WebDriverWait(driver, hp.time_wait)

        th.take_screenshot(driver, name=f"screenshot_{self.browser_name}")

        try:
            # Choose DE language
            wait.until(
                EC.element_to_be_clickable((By.XPATH, hp.top_menu_select_language))
            )
            driver.find_element(By.XPATH, hp.top_menu_select_language).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.btn_lang_de)))
            driver.find_element(By.XPATH, hp.btn_lang_de).click()
            time.sleep(hp.time_mid)

            # Drop Category
            driver.find_element(By.XPATH, hp.top_menu_category_de).click()
            time.sleep(hp.time_min)

            # Check all navigation elements
            for data_test, expected in hp.EXPECTED.items():
                with self.subTest(element=data_test):
                    element = driver.find_element(
                        By.CSS_SELECTOR, f'[data-test="{data_test}"]'
                    )
                    actual = element.text.strip()

                    self.assertEqual(
                        expected,
                        actual,
                        msg=f"[{data_test}] Expected: '{expected}', Actual: '{actual}'",
                    )

        except Exception as e:
            th.take_screenshot(driver, name=f"screenshot_error_{self.browser_name}")
            self.fail(f"The test failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
