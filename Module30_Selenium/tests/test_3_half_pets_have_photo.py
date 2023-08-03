from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_half_pets_have_photo(driver):
    """Проверка, что хотя бы у половины питомцев есть фото"""
    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    # Нажимаем на кнопку перехода на страницу "Мои питомцы"
    driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    # Сохраняем данные из статистики пользователя
    status = driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Установка явного ожидания
    WDW(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr/th/img')))
    # Сохранение всех элементов 'img' в переменную all_pets_images
    all_pets_images = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody/tr/th/img')

    # Получаем количество питомцев из статистики
    pets_number = status[0].text.split('\n')
    pets_number = pets_number[1].split(' ')
    pets_number = int(pets_number[1])

    # Находим половину от всех питомцев
    half = pets_number // 2

    # Находим количество карточек питомцев у которых есть фотография
    number_of_photos = 0
    for i in range(len(all_pets_images)):
        if all_pets_images[i].get_attribute('src') != '':
            number_of_photos += 1

    assert number_of_photos >= half
    print(f'Количество фотографий питомцев: {number_of_photos}')
    print(f'Половина от всех питомцев будет равняться: {half}')
