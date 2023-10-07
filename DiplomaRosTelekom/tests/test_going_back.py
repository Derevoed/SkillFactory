import pytest
from pages.auth_page import AuthPage


"""Кнопка 'Вернуться назад' на странице 'Восстановление пароля' возвращает на страницу авторизации."""


def test_going_back_btn(web_browser):

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.forgot_password_link.click()
    page.wait_page_loaded()

    if page.forgot_password_page_check.is_visible():
        page.going_back_btn.click()
        page.wait_page_loaded()

    assert page.auth_page_check.is_visible()
