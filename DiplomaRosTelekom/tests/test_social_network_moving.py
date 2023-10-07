import pytest
from pages.auth_page import AuthPage


"""Проверки кнопок входа с помощью соцсетей на странице 'Авторизация'. Кнопки переносят на страницы этих соцсетей"""


def test_social_network_vk(web_browser):
    """Проверка перехода на страницу VK"""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.vk_btn.click()
    page.wait_page_loaded()

    assert page.vk_check.is_visible()

    vk_text = page.vk_check.get_text()

    assert vk_text == 'Вход в VK ID'


def test_social_network_ok(web_browser):
    """Проверка перехода на страницу Одноклассников"""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.ok_btn.click()
    page.wait_page_loaded()

    assert page.ok_check.is_visible()

    ok_text = page.ok_check.get_text()

    assert ok_text == 'Одноклассники'


def test_social_network_mail(web_browser):
    """Проверка перехода на страницу Мой Мир@Mail.ru"""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.mail_btn.click()
    page.wait_page_loaded()

    assert page.mymail_check.is_visible()

    my_world_text = page.mymail_check.get_text()

    assert my_world_text == 'Мой Мир@Mail.Ru'


def test_social_network_ya(web_browser):
    """Проверка перехода на страницу Яндекса"""

    page = AuthPage(web_browser)
    page.std_btn.click()
    page.ya_btn.click()
    page.ya_btn.click()     # дублирование команды нажатия второй раз мышкой, иконка перехода срабатывает через раз.
    page.wait_page_loaded()

    assert page.ya_check.is_visible()

    ya_text = page.ya_check.get_text()

    assert ya_text == 'Войдите с Яндекс ID'
