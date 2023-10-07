import pytest
from pages.auth_page import AuthPage


"""Страница 'Авторизация': проверки электронная почта / пароль"""

"""Все тесты рабочие, иногда падают из-за защиты Ростелекома и появляющейся 'капчи' с ошибкой о неверно введенных
 символах с картинки"""


def test_valid_authorisation(web_browser):
    """Попытка входа с валидными данными"""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('testobo@mail.ru')
    page.password.send_keys('pPpEp27zzz^1')
    page.enter_btn.click()
    page.wait_page_loaded()

    # Проверяем, что надпись "Личный кабинет" видна и читаема.
    assert page.lk_text.is_visible()

    lk_text = page.lk_text.get_text()

    assert lk_text == 'Личный кабинет'


def test_empty_fields(web_browser):
    """Оставить оба поля пустыми. Попытка входа. Expected: Сообщение об ошибке."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('')
    page.password.send_keys('')
    page.enter_btn.click()

    # Проверяем наличие ошибки на странице.
    assert page.reg_mail_check.is_visible()

    error_text = page.reg_mail_check.get_text()

    assert error_text == 'Введите адрес, указанный при регистрации'


def test_empty_mail_field(web_browser):
    """Оставить пустое поле 'Электронная почта'. Expected: Сообщение об ошибке"""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('')
    page.password.send_keys('pPpEp27zzz^1')
    page.enter_btn.click()

    # Проверяем наличие ошибки на странице.
    assert page.reg_mail_check.is_visible()

    error_text = page.reg_mail_check.get_text()

    assert error_text == 'Введите адрес, указанный при регистрации'


def test_wrong_password(web_browser):
    """Корректная 'Электронная почта' и некорректный 'Пароль'."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('testobo@mail.ru')
    page.password.send_keys('pPpEp27')
    page.enter_btn.click()
    page.wait_page_loaded()

    # Проверяем наличие ошибки на странице.
    assert page.wrong_log_passw_check.is_visible()

    error_text = page.wrong_log_passw_check.get_text()

    assert error_text == 'Неверный логин или пароль'


def test_wrong_mail(web_browser):
    """Некорректная 'Электронная почта', но корректный 'Пароль'."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('test12o@mail.ru')
    page.password.send_keys('pPpEp27zzz^1')
    page.enter_btn.click()
    page.wait_page_loaded()

    # Проверяем наличие ошибки на странице.
    assert page.wrong_log_passw_check.is_visible()

    error_text = page.wrong_log_passw_check.get_text()

    assert error_text == 'Неверный логин или пароль'


def test_wrong_mail_and_wrong_password(web_browser):
    """Некорректная 'Электронная почта' и некорректный 'Пароль'."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('test12o@mail.ru')
    page.password.send_keys('pPpEp27')
    page.enter_btn.click()
    page.wait_page_loaded()

    # Проверяем наличие ошибки на странице.
    assert page.wrong_log_passw_check.is_visible()

    error_text = page.wrong_log_passw_check.get_text()

    assert error_text == 'Неверный логин или пароль'


def test_opposite_mail_and_password(web_browser):
    """В поле 'Электронная почта' вставить корректный 'Пароль',
    а в поле пароля вставить корректную 'Электронную почту'."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('pPpEp27zzz^1')
    page.password.send_keys('testobo@mail.ru')
    page.enter_btn.click()
    page.wait_page_loaded()

    # Проверяем наличие ошибки на странице.
    assert page.wrong_log_passw_check.is_visible()

    error_text = page.wrong_log_passw_check.get_text()

    assert error_text == 'Неверный логин или пароль'


@pytest.mark.xfail(reason='Падающий тест, ошибка о пустом поле "Пароль" не возникает')
def test_empty_password_field(web_browser):
    """Оставить пустое поле 'Пароль'. Попытка входа. Expected: Сообщение об ошибке."""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.tab_email_btn.click()
    page.user_name.send_keys('testobo@mail.ru')
    page.password.send_keys('')
    page.enter_btn.click()
    page.wait_page_loaded()

    # Проверяем наличие ошибки на странице.
    assert page.wrong_log_passw_check.is_visible()

    error_text = page.wrong_log_passw_check.get_text()

    assert error_text == 'Неверный логин или пароль'
