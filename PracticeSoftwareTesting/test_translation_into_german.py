import os
import random
import string
import time
import unittest

import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helpers as hp
import PracticeSoftwareTesting.helpers as th


class TranslationIntoGermanTest(unittest.TestCase):
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
        if cls.driver:
            cls.driver.quit()

    def test_01_registration(self):
        driver = self.driver
        driver.get(hp.url)
        time.sleep(hp.time_max)
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, hp.time_wait)

        try:
            # Sign in button
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.top_menu_sign_in))
            )
            driver.find_element(By.XPATH, hp.top_menu_sign_in).click()

            # Wait visib login form
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.login_title)))

            # Click to Register your account
            wait.until(
                EC.element_to_be_clickable((By.XPATH, hp.btn_register_your_account))
            )
            driver.find_element(By.XPATH, hp.btn_register_your_account).click()

            # Wait visibl Customer registration
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.customer_registration_title)
                )
            )

            # Рандомные данные для США
            first_names = [
                "James",
                "John",
                "Robert",
                "Michael",
                "William",
                "David",
                "Richard",
                "Joseph",
            ]
            last_names = [
                "Smith",
                "Johnson",
                "Williams",
                "Brown",
                "Jones",
                "Garcia",
                "Miller",
                "Davis",
            ]

            us_cities_states = [
                ("New York", "NY"),
                ("Los Angeles", "CA"),
                ("Chicago", "IL"),
                ("Houston", "TX"),
                ("Phoenix", "AZ"),
                ("Philadelphia", "PA"),
                ("San Antonio", "TX"),
                ("San Diego", "CA"),
                ("Dallas", "TX"),
            ]

            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            birth_year = random.randint(1970, 2000)
            birth_month = str(random.randint(1, 12)).zfill(2)
            birth_day = str(random.randint(1, 28)).zfill(2)
            birth_date = f"{birth_year}-{birth_month}-{birth_day}"

            street_names = [
                "Main St",
                "Oak Ave",
                "Maple Dr",
                "Cedar Ln",
                "Elm St",
                "Pine Rd",
            ]
            street = f"{random.randint(100, 9999)} {random.choice(street_names)}"

            postal_code = str(random.randint(10000, 99999))
            city, state = random.choice(us_cities_states)

            phone = f"1{random.randint(2000000000, 9999999999)}"

            random_suffix = "".join(
                random.choices(string.ascii_lowercase + string.digits, k=8)
            )
            email = f"test_{random_suffix}@example.com"

            special_chars = "@#$%"
            password = (
                "".join(random.choices(string.ascii_uppercase, k=2))
                + "".join(random.choices(string.ascii_lowercase, k=4))
                + "".join(random.choices(string.digits, k=2))
                + random.choice(special_chars)
            )
            password = "".join(random.sample(password, len(password)))

            # Save the email and password
            saved_first_name = first_name
            saved_last_name = last_name
            saved_birth_date = birth_date
            saved_city = city
            saved_state = state
            saved_street = street
            saved_postal_code = postal_code
            saved_phone = phone
            saved_email = email
            saved_password = password

            print(f"first_name: {saved_first_name}")
            print(f"last_name: {saved_last_name}")
            print(f"birth_date: {saved_birth_date}")
            print(f"city: {saved_city}")
            print(f"state: {saved_state}")
            print(f"street: {saved_street}")
            print(f"postal_code: {saved_postal_code}")
            print(f"phone: {saved_phone}")
            print(f"email: {saved_email}")
            print(f"password: {saved_password}")

            # Filling out the form
            # First name
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.first_name_reg_page)))
            driver.find_element(By.XPATH, hp.first_name_reg_page).send_keys(first_name)
            # Last name
            driver.find_element(By.XPATH, hp.last_name_reg_page).send_keys(last_name)
            # Birth date
            driver.find_element(By.XPATH, hp.birth_date_reg_page).send_keys(birth_date)
            # City
            driver.find_element(By.XPATH, hp.city_reg_page).send_keys(city)
            # State
            driver.find_element(By.XPATH, hp.state_reg_page).send_keys(state)
            # Street
            driver.find_element(By.XPATH, hp.street_reg_page).send_keys(street)
            # Postal code
            driver.find_element(By.XPATH, hp.postal_code_reg_page).send_keys(
                postal_code
            )

            # Choosing a country
            driver.find_element(By.XPATH, hp.country_reg_page).click()
            time.sleep(hp.time_mid)
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, hp.dropdown_list_country_reg_page)
                )
            )
            driver.find_element(By.XPATH, hp.dropdown_list_country_reg_page).click()
            time.sleep(hp.time_mid)

            # Phone
            driver.find_element(By.XPATH, hp.phone_reg_page).send_keys(phone)
            # Email address
            driver.find_element(By.XPATH, hp.email_reg_page).send_keys(email)
            # Password
            driver.find_element(By.XPATH, hp.password_reg_page).send_keys(password)

            # Scroll to Register button
            element = driver.find_element(By.XPATH, hp.btn_register_reg_page)
            driver.execute_script("arguments[0].scrollIntoView()", element)

            # Click btn
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.btn_register_reg_page)))
            driver.find_element(By.XPATH, hp.btn_register_reg_page).click()

            # Wait Login form
            wait.until(EC.visibility_of_element_located((By.XPATH, hp.login_title)))

            # Email
            driver.find_element(By.XPATH, hp.email_login_page).send_keys(email)
            # Password
            driver.find_element(By.XPATH, hp.password_login_page).send_keys(password)

            # Click Login btn
            wait.until(EC.element_to_be_clickable((By.XPATH, hp.login_btn_login_page)))
            driver.find_element(By.XPATH, hp.login_btn_login_page).click()

            # My account page

            # Click to Profile btn
            wait.until(
                EC.visibility_of_element_located((By.XPATH, hp.profile_account_page))
            )
            driver.find_element(By.XPATH, hp.profile_account_page).click()
            time.sleep(hp.time_max)

            # First name
            input_text = driver.find_element(
                By.XPATH, hp.input_text_first_name_account_page_filled
            )
            # Getting text from an element
            actual_text = input_text.get_attribute("value")
            # Expected text
            expected_text = saved_first_name
            # Text matching check
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            # Current text output
            print(f"Current data: {actual_text}")

            # Last name
            input_text = driver.find_element(
                By.XPATH, hp.input_text_last_name_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = saved_last_name
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # Email
            input_text = driver.find_element(
                By.XPATH, hp.input_text_email_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = saved_email
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # Phone
            input_text = driver.find_element(
                By.XPATH, hp.input_text_phone_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = saved_phone
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # Country
            input_text = driver.find_element(
                By.XPATH, hp.input_text_country_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = "US"
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # State
            input_text = driver.find_element(
                By.XPATH, hp.input_text_state_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = saved_state
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # City
            input_text = driver.find_element(
                By.XPATH, hp.input_text_city_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = saved_city
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # Street
            input_text = driver.find_element(
                By.XPATH, hp.input_text_street_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = saved_street
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

            # Postal code
            input_text = driver.find_element(
                By.XPATH, hp.input_text_postal_code_account_page_filled
            )
            actual_text = input_text.get_attribute("value")
            expected_text = saved_postal_code
            assert actual_text == expected_text, (
                f"The data in the input field does not match what is expected. Expected: '{expected_text}', Actually: '{actual_text}'"
            )
            print(f"Current data: {actual_text}")

        except Exception as e:
            th.take_screenshot(driver, name=f"screenshot_error_{self.browser_name}")
            self.fail(f"The test failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
