import pytest
from pages.auth_page import AuthPage
from data_testing.values import tel_1_num, tel_4_num, tel_10_num, tel_11_num, tel_12_num, tel_13_num
from data_testing.values import tel_pos_1, tel_pos_2, tel_pos_3, tel_pos_4, tel_pos_5, tel_pos_6, tel_pos_7, tel_pos_8
from data_testing.values import tel_pos_9, reference_number_1, reference_number_2


"""Страница 'Авторизация': проверки поля ввода телефона"""


@pytest.mark.parametrize('telephone', [tel_1_num, tel_4_num, tel_10_num])
def test_telephone_field_negative(web_browser, telephone):
    """Негативные проверки поля ввода 'Телефона'."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.wait_page_loaded()
    page.tab_tel_btn.click()
    page.user_name.send_keys(telephone)
    page.password.click()

    # Проверяем наличие ошибки на странице.
    assert page.wrong_tel_check.is_visible()

    error_text = page.wrong_tel_check.get_text()

    assert error_text == 'Неверный формат телефона'


@pytest.mark.parametrize('telephone', [tel_pos_1, tel_pos_2, tel_pos_3, tel_pos_4, tel_pos_5, tel_pos_6,
                                       tel_pos_7, tel_pos_8, tel_pos_9])
def test_telephone_field_positive(web_browser, telephone):
    """Позитивные проверки поля ввода 'Телефона' функции автозамены на стандартное написание номера."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.wait_page_loaded()
    page.tab_tel_btn.click()
    page.user_name.send_keys(telephone)
    page.password.click()

    # Проверяем отсутствие надписи с ошибкой под полем ввода.
    if page.wrong_tel_check.is_visible() is not True:
        error_present = 0  # Ошибки нет
    else:
        error_present = 1  # Ошибка присутствует

    assert error_present == 0

    # Проверяем соответствуют ли принятые и выведенные данные на поле ввода шаблонному (эталонному номеру), авто-подмена
    inserted_tel = page.inserted_tel_auth.get_attribute('value')

    assert inserted_tel == reference_number_1 or inserted_tel == reference_number_2
