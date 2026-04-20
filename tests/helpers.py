import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_chrome():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def create_firefox():
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/firefox"
    os.environ["MOZ_HEADLESS"] = "1"
    service = webdriver.FirefoxService(executable_path="/usr/local/bin/geckodriver")
    return webdriver.Firefox(options=options, service=service)


def create_edge():
    options = EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-data-dir=/tmp/edge-profile")
    service = webdriver.EdgeService(executable_path="/usr/local/bin/msedgedriver")
    return webdriver.Edge(options=options, service=service)


DRIVERS = {
    "chrome": create_chrome,
    "firefox": create_firefox,
    "edge": create_edge,
}
