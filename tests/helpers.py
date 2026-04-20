from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


def create_chrome():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    service = ChromeService()
    return webdriver.Chrome(service=service, options=options)


def create_firefox():
    """Firefox требует специальной конфигурации для headless режима"""
    options = FirefoxOptions()
    options.add_argument("--headless")
    # Эти опции специфичны для Firefox
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)

    # Указываем корректный путь к Firefox
    options.binary_location = "/usr/bin/firefox"

    # Используем geckodriver с явным путем
    service = FirefoxService(executable_path="/usr/local/bin/geckodriver")

    try:
        return webdriver.Firefox(service=service, options=options)
    except Exception as e:
        print(f"Firefox initialization error: {e}")
        # Пробуем без явного пути к geckodriver
        return webdriver.Firefox(options=options)


def create_edge():
    options = EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-data-dir=/tmp/edge-profile")
    service = EdgeService(executable_path="/usr/local/bin/msedgedriver")
    return webdriver.Edge(service=service, options=options)


DRIVERS = {
    "chrome": create_chrome,
    "firefox": create_firefox,
    "edge": create_edge,
}
