from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets_have_different_names(driver):
    """Проверка, что у всех питомцев разные имена"""
    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    # Нажимаем на кнопку перехода на страницу "Мои питомцы"
    driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="table table-hover"]/tbody/tr')))
    # Сохранение всех данных о питомцах в переменную my_pets_data
    my_pets_data = driver.find_elements(By.XPATH, '//*[@class="table table-hover"]/tbody/tr')

    # Перебираем данные о питомцах и убираем лишние элементы
    pets_names = []
    for i in range(len(my_pets_data)):
        pets_info = my_pets_data[i].text.replace('\n', '').replace('×', '')
        # Разделяем элементы пробелом
        split_data_pet = pets_info.split(' ')
        # Добавляем имена питомцев в отдельный список
        pets_names.append(split_data_pet[0])

    print(f'Все имена питомцев', pets_names)

    # Перебираем и проверяем все имена на повторения, при наличии повтора добавляем +1 к счетчику 'repeated_names'
    repeated_names = 0
    for i in range(len(pets_names)):
        if pets_names.count(pets_names[i]) > 1:
            repeated_names += 1
    # Проверяем что повторяющихся имен нет
    assert repeated_names == 0, print(f'Количество повторений в именах питомцев', repeated_names)

