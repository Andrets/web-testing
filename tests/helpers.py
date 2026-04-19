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
    return webdriver.Firefox(options=options)


def create_edge():
    options = EdgeOptions()
    options.add_argument("--headless")
    return webdriver.Edge(options=options)


DRIVERS = {
    "chrome": create_chrome,
    "firefox": create_firefox,
    "edge": create_edge,
}
