import pytest
from pages.registration_page import RegPage
from data_testing.values import tel_1_num, tel_4_num, tel_10_num, tel_11_num, tel_12_num, tel_13_num
from data_testing.values import tel_pos_1, tel_pos_2, tel_pos_3, tel_pos_4, tel_pos_5, tel_pos_6, tel_pos_7, tel_pos_8
from data_testing.values import tel_pos_9, reference_number_1, reference_number_2
from data_testing.values import email_neg_1, email_neg_2, email_neg_3, email_neg_4, email_neg_5, email_neg_6
from data_testing.values import email_neg_7, email_neg_8, email_neg_9, email_pos_1, email_pos_2, email_pos_3
from data_testing.values import email_pos_4, email_pos_5, email_pos_6, email_pos_7, email_pos_8


"""Страница 'Регистрация': проверки поля ввода 'E-mail или мобильный телефон'."""


@pytest.mark.parametrize('telephone', [tel_1_num, tel_4_num, tel_10_num, tel_11_num, tel_12_num, tel_13_num])
def test_telephone_field_negative(web_browser, telephone):
    """Негативные проверки поля ввода 'Телефона'."""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.email_field.send_keys(telephone)
    page.password_field.click()

    # Проверяем наличие ошибки на странице.
    assert page.check_tel_mail.is_visible()

    error_text = page.check_tel_mail.get_text()

    assert error_text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                         'или email в формате example@email.ru'


@pytest.mark.parametrize('telephone', [tel_pos_1, tel_pos_2, tel_pos_3, tel_pos_4, tel_pos_5, tel_pos_6,
                                       tel_pos_7, tel_pos_8, tel_pos_9])
def test_telephone_field_positive(web_browser, telephone):
    """Позитивные проверки поля ввода 'Телефона' функции автозамены на стандартное написание номера."""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.email_field.send_keys(telephone)
    page.password_field.click()

    # Проверяем отсутствие надписи с ошибкой под полем ввода.
    if page.check_tel_mail.is_visible() is not True:
        error_present = 0  # Ошибки нет
    else:
        error_present = 1  # Ошибка присутствует

    assert error_present == 0

    # Проверяем соответствуют ли принятые и выведенные данные на поле ввода шаблонному (эталонному номеру), авто-подмена
    inserted_tel = page.inserted_tel.get_attribute('value')

    assert inserted_tel == reference_number_1 or inserted_tel == reference_number_2


@pytest.mark.parametrize('e_mail', ['', email_neg_1, email_neg_2, email_neg_3, email_neg_4,
                                    email_neg_5, email_neg_6, email_neg_7])
def test_email_field_negative(web_browser, e_mail):
    """Негативные проверки поля ввода 'E-mail'."""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.email_field.send_keys(e_mail)
    page.registration_btn.click()

    # Проверяем наличие ошибки на странице.
    assert page.check_tel_mail.is_visible()

    error_text = page.check_tel_mail.get_text()

    assert error_text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                         'или email в формате example@email.ru'


@pytest.mark.xfail(reason='Поле ввода E-mail позволяет ввести электронную почту длинной более 320 символов')
@pytest.mark.parametrize('e_mail', [email_neg_8, email_neg_9])
def test_email_field_negative_320_symbols(web_browser, e_mail):
    """Негативные проверки поля ввода 'E-mail', ввод почты длинной > 320-ти символов."""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.email_field.send_keys(e_mail)
    page.registration_btn.click()

    # Проверяем наличие ошибки на странице.
    assert page.check_tel_mail.is_visible()

    error_text = page.check_tel_mail.get_text()

    assert error_text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                         'или email в формате example@email.ru'


@pytest.mark.parametrize('e_mail', [email_pos_1, email_pos_2, email_pos_3, email_pos_4,
                                    email_pos_5, email_pos_6, email_pos_7, email_pos_8])
def test_email_field_positive(web_browser, e_mail):
    """Позитивные проверки поля ввода 'E-mail'."""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.email_field.send_keys(e_mail)
    page.registration_btn.click()

    # Проверяем отсутствие надписи с ошибкой под полем ввода.
    if page.check_tel_mail.is_visible() is not True:
        error_present = 0  # Ошибки нет
    else:
        error_present = 1  # Ошибка присутствует

    assert error_present == 0
