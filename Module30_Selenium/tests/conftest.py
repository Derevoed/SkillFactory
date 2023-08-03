import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password


@pytest.fixture()
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://petfriends.skillfactory.ru/login')
    # Установка неявного ожидания
    element = driver.find_element(By.ID, 'email')
    element.send_keys(valid_email)
    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    yield driver

    driver.quit()
