import os
import unittest

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import tests.helpers as th


class SearchAppleSiteTest(unittest.TestCase):
    driver: webdriver.Remote

    @classmethod
    def setUpClass(cls):
        browser = os.environ.get("BROWSER", "chrome").lower()
        if browser not in th.DRIVERS:
            raise ValueError(f"Unsupported browser: {browser}")
        cls.driver = th.DRIVERS[browser]()
        cls.driver.maximize_window()
        allure.dynamic.parameter("browser", browser)

    def test_search_apple_site(self):
        """Open Apple.com and check having navigation bar"""
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get("https://www.apple.com/")

        try:
            # Дождитесь завершения загрузки страницы
            wait.until(
                lambda driver: (
                    driver.execute_script("return document.readyState") == "complete"
                )
            )

            # Дождитесь появления элемента
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.globalnav"))
            )
        except AssertionError as e:
            # Сохраняем скриншот при ошибке
            print(e)
            self.fail("The test failed: an authorization issue")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
