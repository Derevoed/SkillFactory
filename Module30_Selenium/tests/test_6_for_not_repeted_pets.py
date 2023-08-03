from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_for_not_repeated_pets(driver):
    """Проверка, что в списке нет повторяющихся питомцев."""
    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    # Нажимаем на кнопку перехода на страницу "Мои питомцы"
    driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="table table-hover"]/tbody/tr')))
    # Сохранение всех данных о питомцах в переменную my_pets_data
    my_pets_data = driver.find_elements(By.XPATH, '//*[@class="table table-hover"]/tbody/tr')

    # Перебираем данные о питомцах и убираем лишние элементы
    pets_all_data = []
    for i in range(len(my_pets_data)):
        pets_info = my_pets_data[i].text.replace('\n', '').replace('×', '')
        # Разделяем элементы пробелом
        split_data_pet = pets_info.split(' ')
        # Добавляем данные питомцев в отдельный список
        pets_all_data.append(split_data_pet)

    # Данные по каждому питомцу объединяем в одно 'слово', 'слова' разделяем пробелами
    data_line = ''
    for i in pets_all_data:
        data_line += ''.join(i)
        data_line += ' '

    # Создаем список из строки
    row_list = data_line.split(' ')

    # Создаем из списка множество для отображения только уникальных значений
    set_row_list = set(row_list)

    # Находим количество элементов в списке и в множестве
    row_list_number = len(row_list)
    set_row_list_number = len(set_row_list)

    # Вычитаем одно значение из другого, так как в множестве только уникальные значения, то при наличии повторений в
    # списке результат будет не равный нулю.
    difference = row_list_number - set_row_list_number
    assert difference == 0, print(f'В списке есть одинаковые питомцы')
