import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
from datetime import date
import time
import unittest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Класс для тестирования в Chrome
class ChromeSearch(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # Настройка Chrome
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Headless режим
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Отладочный вывод пути к ChromeDriver
        chromedriver_path = ChromeDriverManager().install()
        print(f"ChromeDriver path: {chromedriver_path}")
        # Ручное исправление пути
        if not chromedriver_path.endswith("chromedriver"):
            chromedriver_path = "/home/runner/.wdm/drivers/chromedriver/linux64/134.0.6998.165/chromedriver-linux64/chromedriver"
            print(f"Fixed ChromeDriver path: {chromedriver_path}")
        cls.driver = webdriver.Chrome(
            service=Service(chromedriver_path),
            options=options
        )
        cls.driver.maximize_window()

    def test_search_apple_site(self):
        '''Open Apple.com and check having navigation bar in Chrome'''
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        driver.get('https://www.apple.com/')

        # Сохраняем скриншот для отладки
        driver.save_screenshot("apple_homepage_chrome.png")

        try:
            # Дождитесь завершения загрузки страницы
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

            # Дождитесь появления элемента
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.globalnav")))
        except Exception as e:
            # Сохраняем скриншот при ошибке
            driver.save_screenshot("error_screenshot_chrome.png")
            raise
    
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

# Класс для тестирования в Yandex
class YandexSearch(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # Настройка Yandex
        service = Service('/usr/local/bin/yandexdriver')
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/yandex-browser'
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()


    def test_search_apple_site(self):
        '''Open Apple.com and check having navigation bar in Yandex'''
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        driver.get('https://www.apple.com/')

        # Сохраняем скриншот для отладки
        driver.save_screenshot("apple_homepage_yandex.png")

        try:
            # Дождитесь завершения загрузки страницы
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

            # Дождитесь появления элемента
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.globalnav")))
        except Exception as e:
            # Сохраняем скриншот при ошибке
            driver.save_screenshot("error_screenshot_yandex.png")
            raise

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

# Класс для тестирования в Edge
class EdgeSearch(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # Настройка Edge
        options = EdgeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Edge(options=options)
        cls.driver.maximize_window()


    def test_search_apple_site(self):
        '''Open Apple.com and check having navigation bar in Edge'''
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        driver.get('https://www.apple.com/')

        # Сохраняем скриншот для отладки
        driver.save_screenshot("apple_homepage_edge.png")

        try:
            # Дождитесь завершения загрузки страницы
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

            # Дождитесь появления элемента
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.globalnav")))
        except Exception as e:
            # Сохраняем скриншот при ошибке
            driver.save_screenshot("error_screenshot_edge.png")
            raise
    
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()


if __name__ == '__main__':
    unittest.main()