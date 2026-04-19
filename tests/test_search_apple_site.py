import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    def test_search_apple_site(self):
        """Open Apple.com and check having navigation bar"""
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get("https://www.apple.com/")

        # Сохраняем скриншот для отладки
        driver.save_screenshot("apple_homepage.png")

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
        except Exception as e:
            # Сохраняем скриншот при ошибке
            driver.save_screenshot("error_screenshot.png")
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


def take_screenshot(driver, name):
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
    driver.save_screenshot(screenshot_path)


if __name__ == "__main__":
    unittest.main()
