import pytest
from pages.registration_page import RegPage
from data_testing.values import line255, line31, kir_line31, kir_line255, line_4_16, line_16_4
from data_testing.values import kir_line10, kir_line10_dash, kir_line29, kir_line29_dash, kir_line30, kir_line30_dash


"""Страница 'Регистрация': проверки полей ввода 'Имя', 'Фамилия'."""


@pytest.mark.parametrize('name', ['И', 'I', '1', '原', '?'])
def test_one_symbol_name_field(web_browser, name):
    """Поле ввода 'Имя' не допускает ввод строки длинной менее 2 символов"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.name_field.send_keys(name)
    page.email_field.click()

    assert page.check_name.is_visible()

    error_text = page.check_name.get_text()

    assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.parametrize('last_name', ['И', 'I', '1', '原', '?'])
def test_one_symbol_last_name_field(web_browser, last_name):
    """Поле ввода 'Фамилия' не допускает ввод строки длинной менее 2 символов"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(last_name)
    page.email_field.click()

    assert page.check_name.is_visible()

    error_text = page.check_name.get_text()

    assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.parametrize('name', [kir_line31, kir_line255, line31, line255])
def test_more_than_30_symbols_name_field(web_browser, name):
    """Поле ввода 'Имя' не допускает ввод строки длинной более 30 символов. Пробуем ввести строки длинной 30 и 255
    символов только кириллицей, кириллицей и латиницей и числами"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.name_field.send_keys(name)
    page.email_field.click()

    assert page.check_name.is_visible()

    error_text = page.check_name.get_text()

    assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.parametrize('last_name', [kir_line31, kir_line255, line31, line255])
def test_more_than_30_symbols_last_name_field(web_browser, last_name):
    """Поле ввода 'Фамилия' не допускает ввод строки длинной более 30 символов. Пробуем ввести строки длинной 30 и 255
    символов только кириллицей, кириллицей и латиницей и числами"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(last_name)
    page.email_field.click()

    assert page.check_name.is_visible()

    error_text = page.check_name.get_text()

    assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.xfail(reason='Поле не принимает слово больше 15 символов в составных словах через тире, '
                          'как и слова из трех букв в формате "*-**" ')
@pytest.mark.parametrize('name', ['Ли', 'ЛиИ', 'Ли-И', 'Л-Ии', kir_line10, kir_line10_dash, kir_line29,
                                  kir_line29_dash, kir_line30, kir_line30_dash, line_4_16, line_16_4])
def test_name_field_with_valid_data(web_browser, name):
    """Позитивные проверки поля ввода 'Имя'. Ввод строки кириллицей длинной: 2, 3, 10, 29, 30 символов,
    ввод строки разделенной знаком тире (-), проверка составного слова 4 + 16 символов через тире (поле не принимает
    строку больше 15 символов в составных словах)"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.name_field.send_keys(name)
    page.email_field.click()

    # Проверяем отсутствие надписи с ошибкой под полем ввода.
    if page.check_name.is_visible() is not True:
        error_present = 0   # Ошибки нет
    else:
        error_present = 1   # Ошибка присутствует

    assert error_present == 0


@pytest.mark.xfail(reason='Поле не принимает слово больше 15 символов в составных словах через тире, '
                          'как и слова из трех букв в формате "*-**" ')
@pytest.mark.parametrize('last_name', ['Ли', 'ЛиИ', 'Ли-И', 'Л-Ии', kir_line10, kir_line10_dash, kir_line29,
                                       kir_line29_dash, kir_line30, kir_line30_dash, line_4_16, line_16_4])
def test_last_name_field_with_valid_data(web_browser, last_name):
    """Позитивные проверки поля ввода 'Фамилия'. Ввод строки кириллицей длинной: 2, 3, 10, 29, 30 символов,
    ввод строки разделенной знаком тире (-), проверка составного слова 4 + 16 символов через тире (поле не принимает
    строку больше 15 символов в составных словах)"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(last_name)
    page.email_field.click()

    # Проверяем отсутствие надписи с ошибкой под полем ввода.
    if page.check_name.is_visible() is not True:
        error_present = 0   # Ошибки нет
    else:
        error_present = 1   # Ошибка присутствует

    assert error_present == 0


@pytest.mark.parametrize('name', ['123', 'Дмитрий1', 'Ivan', '☺☻♥♦', '№%6?'])
def test_name_field_negative(web_browser, name):
    """Поле ввода 'Имя' не допускает ввод числовых символов, символов альтернативной клавиатуры и букв латиницей"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.name_field.send_keys(name)
    page.email_field.click()

    assert page.check_name.is_visible()

    error_text = page.check_name.get_text()

    assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.parametrize('name', ['123', 'Дмитрий1', 'Ivan', '☺☻♥♦', '№%6?'])
def test_last_name_field_negative(web_browser, name):
    """Поле ввода 'Фамилия' не допускает ввод числовых символов, символов альтернативной клавиатуры и букв латиницей"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(name)
    page.email_field.click()

    assert page.check_name.is_visible()

    error_text = page.check_name.get_text()

    assert error_text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
