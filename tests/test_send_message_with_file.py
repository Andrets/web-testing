import os
import time
import unittest

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helpers as hp
import tests.helpers as th


class BaseTest(unittest.TestCase):
    driver: webdriver.Remote

    @classmethod
    def setUpClass(cls):
        browser = os.environ.get("BROWSER", "chrome").lower()
        if browser not in th.DRIVERS:
            raise ValueError(f"Unsupported browser: {browser}")
        cls.driver = th.DRIVERS[browser]()
        cls.driver.maximize_window()
        allure.dynamic.parameter("browser", browser)

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

        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_homepage",
            attachment_type=allure.attachment_type.PNG,
        )

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
            allure.attach(
                driver.get_screenshot_as_png(),
                name="error_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            self.fail(f"The test failed: {str(e)}")


def take_screenshot(driver, name):
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
    driver.save_screenshot(screenshot_path)


if __name__ == "__main__":
    unittest.main()
