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
        browser = os.getenv('BROWSER', 'chrome').lower()
        
        if browser == 'chrome':
            options = ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            chromedriver_path = ChromeDriverManager().install()
            print(f"ChromeDriver path: {chromedriver_path}")
            cls.driver = webdriver.Chrome(
							service=Service(chromedriver_path),
							options=options
						)
        elif browser == 'yandex':
            service = Service('/usr/local/bin/yandexdriver')
            options = ChromeOptions()
            cls.driver = webdriver.Chrome(service=service, options=options)
        elif browser == 'edge':
            options = EdgeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            cls.driver = webdriver.Edge(options=options)
        elif browser == 'firefox':
            options = FirefoxOptions()
            cls.driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f'Unsupported browser: {browser}')
        
        cls.driver.maximize_window()
    
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
    
    def test_search_apple_site(self):
        '''Open Apple.com and check having navigation bar'''
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get('https://www.apple.com/')
        wait.until(EC.visibility_of_element_located((By.XPATH, "//nav[@class='globalnav js']")))


if __name__ == '__main__':
    unittest.main()