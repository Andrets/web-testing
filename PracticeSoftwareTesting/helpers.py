import os
import time

import allure
from selenium import webdriver


def create_options(browser_name):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Set window size to 1920x1080
    options.add_argument("--window-size=1920,1080")

    # Disable automation switches to avoid detection
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Use automation-friendly user agent
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # must for docker
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return options


def create_chrome():
    chrome_options = webdriver.ChromeOptions()
    """Connect to Chrome via Selenium Grid"""
    hub_url = os.environ.get("SELENIUM_HUB", "http://localhost:4444")
    chrome_options.set_capability("browserName", "chrome")
    chrome_options = create_options("chrome")
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
    edge_options = create_options("edge")
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
