import pytest
from pages.registration_page import RegPage


"""Страница 'Регистрация': попытка зарегистрировать нового пользователя с уже используемым электронным ящиком."""


def test_try_to_registrate_new_user_with_registered_email(web_browser):
    """Проверка невозможности регистрации нового пользователя на платформе "Ростелеком" с использованием e-mail
    уже зарегистрированного пользователя"""

    page = RegPage(web_browser)
    page.std_btn.click()
    page.reg_link.click()
    page.wait_page_loaded()
    page.name_field.send_keys('Том')
    page.last_name_field.send_keys('Джерри')
    page.email_field.send_keys('testobo@mail.ru')   # Вводим уже зарегистрированный E-mail
    page.password_field.send_keys('pPpEp27zzz^123')
    page.confirm_password_field.send_keys('pPpEp27zzz^123')
    page.registration_btn.click()

    tx = page.check_user_exist.get_text()

    # Проверяем что на экране появилось pop-up сообщение с текстом "Учётная запись уже существует"
    assert tx == 'Учётная запись уже существует'
