from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets_are_present(driver):
    """Проверка, что количество карточек питомцев соответствует количеству питомцев из статистики"""
    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    # Нажимаем на кнопку перехода на страницу "Мои питомцы"
    driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    # Сохраняем данные из статистики пользователя
    status = driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="table table-hover"]/tbody/tr')))
    # Сохранение карточек питомцев в переменную
    pets = driver.find_elements(By.XPATH, '//*[@class="table table-hover"]/tbody/tr')

    # Получаем количество питомцев из статистики
    pets_number = status[0].text.split('\n')
    pets_number = pets_number[1].split(' ')
    pets_number = int(pets_number[1])

    # Находим количество карточек питомцев
    pet_cards = len(pets)
    print(pet_cards)

    # Сверяем, что количество карточек питомцев соответствует количеству питомцев из статистики
    assert pets_number == pet_cards
