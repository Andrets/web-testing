import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helpers as hp


class WebAuthorization:
    def __init__(self, driver):
        self.driver = driver

    def test_web_authorization(self):
        if not self.driver:
            raise ValueError("Driver not initialized.")

        driver = self.driver
        driver.get(hp.url)
        time.sleep(hp.time_max)
        driver = self.driver
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, hp.time_wait)

        try:
            # Click to sign in btn
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.top_menu_sign_in)))
            driver.find_element(By.XPATH, hp.top_menu_sign_in).click()

            # email
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.email_login_page))
            )
            driver.find_element(By.XPATH, hp.email_login_page).send_keys(hp.admin_email)

            # password
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.password_login_page)))
            driver.find_element(By.XPATH, hp.password_login_page).send_keys(
                hp.admin_password
            )

            wait.until(EC.element_to_be_clickable((By.XPATH, hp.login_btn_login_page)))
            driver.find_element(By.XPATH, hp.login_btn_login_page).click()

            # Waiting for the end of authorization
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.top_menu_home)))

        except Exception as e:
            raise AssertionError(f"Authorization error: {str(e)}")
