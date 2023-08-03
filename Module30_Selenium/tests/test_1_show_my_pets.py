from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


import time


def test_show_my_pets(driver):
    """Проверка, что переход на страницу 'Мои питомцы' осуществляется"""

    # Проверяем, что мы находимся на главной странице ресурса
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    # Нажимаем на кнопку перехода на страницу "Мои питомцы"
    driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Проверяем, что мы оказались на странице пользователя "Мои питомцы"
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    time.sleep(3)
