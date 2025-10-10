import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language: es, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    
    # Принудительно очищаем кэш и устанавливаем свежую версию
    from webdriver_manager.core.os_manager import ChromeType
    driver_path = ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
    
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    
    service = Service(driver_path)
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(10)
    
    yield browser
    browser.quit()