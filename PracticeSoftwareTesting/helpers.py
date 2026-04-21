import os
import time

import allure
from selenium import webdriver


def create_chrome():
    chrome_options = webdriver.ChromeOptions()
    """Connect to Chrome via Selenium Grid"""
    hub_url = os.environ.get("SELENIUM_HUB", "http://localhost:4444")
    chrome_options.set_capability("browserName", "chrome")
    return webdriver.Remote(
        command_executor=f"{hub_url}/wd/hub", options=chrome_options
    )


def create_firefox():
    firefox_options = webdriver.FirefoxOptions()
    """Connect to Firefox via Selenium Grid"""
    hub_url = os.environ.get("SELENIUM_HUB", "http://localhost:4444")
    firefox_options.set_capability("browserName", "firefox")
    firefox_options.set_capability("acceptInsecureCerts", True)
    firefox_options.set_capability("moz:debuggerAddress", True)
    return webdriver.Remote(
        command_executor=f"{hub_url}/wd/hub", options=firefox_options
    )


def create_edge():
    edge_options = webdriver.EdgeOptions()
    """Connect to Edge via Selenium Grid"""
    hub_url = os.environ.get("SELENIUM_HUB", "http://localhost:4444")
    edge_options.set_capability("browserName", "MicrosoftEdge")
    return webdriver.Remote(command_executor=f"{hub_url}/wd/hub", options=edge_options)


DRIVERS = {
    "chrome": create_chrome,
    "firefox": create_firefox,
    "edge": create_edge,
}


def take_screenshot(driver: webdriver.Remote, name="screenshot"):
    os.makedirs("screenshots", exist_ok=True)

    timestamp = int(time.time())
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join("screenshots", filename)

    # 1. Сохраняем файл (для artifact)
    driver.save_screenshot(filepath)

    # 2. Прикрепляем в Allure
    with open(filepath, "rb") as f:
        allure.attach(
            f.read(), name=filename, attachment_type=allure.attachment_type.PNG
        )
