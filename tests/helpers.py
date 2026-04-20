import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def create_chrome():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if os.environ.get("GITHUB_ACTIONS"):
        return webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub", options=options
        )
    return webdriver.Chrome(options=options)


def create_firefox():
    options = FirefoxOptions()
    options.add_argument("--headless")

    if os.environ.get("GITHUB_ACTIONS"):
        return webdriver.Remote(
            command_executor="http://firefox:4444/wd/hub", options=options
        )
    return webdriver.Firefox(options=options)


def create_edge():
    options = EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if os.environ.get("GITHUB_ACTIONS"):
        return webdriver.Remote(
            command_executor="http://edge:4444/wd/hub", options=options
        )
    return webdriver.Edge(options=options)


DRIVERS = {
    "chrome": create_chrome,
    "firefox": create_firefox,
    "edge": create_edge,
}
