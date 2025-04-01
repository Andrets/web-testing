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

class BaseTest(unittest.TestCase):
    driver = None
     
    @classmethod
    def setUpClass(cls):
        browser = cls.browser
        
        if browser == 'chrome':
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
        elif browser == 'yandex':
            service = Service('/usr/local/bin/yandexdriver')
            options = ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.binary_location = '/usr/bin/yandex-browser'
            cls.driver = webdriver.Chrome(service=service, options=options)
        elif browser == 'edge':
            options = EdgeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            cls.driver = webdriver.Edge(options=options)
        elif browser == 'firefox':
            options = FirefoxOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            cls.driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f'Unsupported browser: {browser}')
        
        cls.driver.maximize_window()
    
    def test_search_apple_site(self):
        '''Open Apple.com and check having navigation bar'''
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get('https://www.apple.com/')
        
        # Сохраняем скриншот для отладки
        driver.save_screenshot(f"apple_homepage_{self.browser}.png")
        
        try:
            # Дождитесь завершения загрузки страницы
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            
            # Дождитесь появления элемента
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.globalnav")))
        except Exception as e:
            # Сохраняем скриншот при ошибке
            driver.save_screenshot(f"error_screenshot_{self.browser}.png")
            raise
    
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

def create_test_class(browser_name):
    class_name = f"{browser_name.capitalize()}Search"
    return type(class_name, (BaseTest,), {'browser': browser_name})

BROWSERS = ['chrome', 'yandex', 'edge']

for browser in BROWSERS:
    globals()[f"{browser.capitalize()}Search"] = create_test_class(browser)

if __name__ == '__main__':
    unittest.main()