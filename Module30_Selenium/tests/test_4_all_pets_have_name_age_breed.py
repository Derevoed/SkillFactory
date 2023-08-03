from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets_have_name_age_breed(driver):
    """Проверка, что у всех питомцев есть имя, возраст и порода"""
    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    # Нажимаем на кнопку перехода на страницу "Мои питомцы"
    driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="table table-hover"]/tbody/tr')))
    # Сохранение всех данных о питомцах в переменную my_pets_data
    my_pets_data = driver.find_elements(By.XPATH, '//*[@class="table table-hover"]/tbody/tr')

    # Перебираем данные о питомцах и убираем лишние элементы
    for i in range(len(my_pets_data)):
        pets_info = my_pets_data[i].text.replace('\n', '').replace('×', '')
        # Разделяем элементы пробелом
        split_data_pet = pets_info.split(' ')
        # Находим количество элементов в списке и сравниваем с ожидаемым результатом (имя, возраст, порода = 3)
        result = len(split_data_pet)
        assert result == 3
        