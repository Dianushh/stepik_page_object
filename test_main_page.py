from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    
    # Добавим небольшую задержку для стабильности
    time.sleep(2)
    
    # Находим и кликаем на ссылку логина
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    
    # Проверяем, что перешли на страницу логина
    WebDriverWait(browser, 10).until(
        EC.url_contains("login")
    )
    
    # Можно добавить проверку, что страница загрузилась
    assert "login" in browser.current_url