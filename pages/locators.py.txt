from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")