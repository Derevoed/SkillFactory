import pytest
from pages.auth_page import AuthPage


"""Ссылка "пользовательского соглашения" на странице "Авторизация" открывает новую страницу с текстом 
о пользовательском соглашении."""


def test_agreement_link(web_browser):
    """Проверка перехода на страницу пользовательского соглашения"""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.wait_page_loaded()
    page.agreement_link.click()
    page.wait_page_loaded()
    page.switch_to_new_window()

    url = page.get_current_url()

    # Сравниваем текущий адрес новой, открытой страницы с адресом страницы пользовательского соглашения.
    assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    agreement_text = page.agreement_check.get_text()

    # Сверяем заголовок на странице с заголовком пользовательского соглашения.
    assert agreement_text == 'Публичная оферта о заключении Пользовательского соглашения на использование ' \
                             'Сервиса «Ростелеком ID»'
