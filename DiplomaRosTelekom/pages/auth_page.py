from pages.base import WebPage
from pages.elements import WebElement


"""Страница авторизации"""


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://lk.rt.ru/'
        super().__init__(web_driver, url)

    # Кнопка войти с паролем на стартовой странице
    std_btn = WebElement(id='standard_auth_btn')

    # Кнопка табуляции почта
    tab_email_btn = WebElement(id='t-btn-tab-mail')

    # Кнопка табуляции телефон
    tab_tel_btn = WebElement(id='t-btn-tab-phone')

    # Поле ввода логина
    user_name = WebElement(id='username')

    # Поле ввода пароля
    password = WebElement(id='password')

    # Кнопка Войти
    enter_btn = WebElement(id="kc-login")

    # Надпись Личный кабинет
    lk_text = WebElement(xpath='//div[@class="StyledHeaderTopPartMenuItemLk-kHgfwO lfjrSy"]')

    # Кнопки перехода в соцсети: VK, Одноклассники, Mail.ru, Yandex
    vk_btn = WebElement(id='oidc_vk')
    ok_btn = WebElement(id='oidc_ok')
    mail_btn = WebElement(id='oidc_mail')
    ya_btn = WebElement(id='oidc_ya')

    # Элементы проверки перехода на страницы соцсетей
    vk_check = WebElement(xpath='//div[contains(text(), "Вход в VK ID")]')
    ok_check = WebElement(xpath='//div[contains(text(), "Одноклассники")]')
    mymail_check = WebElement(xpath='//span[contains(text(), "Мой Мир@Mail.Ru")]')
    ya_check = WebElement(xpath='//h1[contains(text(), "Яндекс ID")]')

    # Ссылка пользовательского соглашения
    agreement_link = WebElement(id='rt-auth-agreement-link')

    # Проверка перехода на страницу пользовательского соглашения
    agreement_check = WebElement(xpath='//h1[@class="offer-title"]')

    # Появляющаяся надпись "Неверный формат телефона"
    wrong_tel_check = WebElement(xpath='//span[contains(text(), "Неверный формат телефона")]')

    # Введенный телефон
    inserted_tel_auth = WebElement(xpath='//input[@name="username"]')

    # Появляющаяся надпись "Введите адрес, указанный при регистрации"
    reg_mail_check = WebElement(xpath='//span[contains(text(), "Введите адрес, указанный при регистрации")]')

    # Появляющееся сообщение "Неверный логин или пароль"
    wrong_log_passw_check = WebElement(xpath='//span[contains(text(), "Неверный логин или пароль")]')

    # Появляющееся сообщение "Неверно введен текст с картинки"
    wrong_picture_text = WebElement(xpath='//span[contains(text(), "Неверно введен текст с картинки")]')

    # Ссылка "Забыл пароль"
    forgot_password_link = WebElement(id='forgot_password')

    # Проверка перехода на страницу восстановления пароля
    forgot_password_page_check = WebElement(xpath='//h1[contains(text(), "Восстановление Пароля")]')

    # Кнопка "Вернуться назад на странице восстановления пароля"
    going_back_btn = WebElement(id='reset-back')

    # Проверка нахождения на странице "Авторизации"
    auth_page_check = WebElement(xpath='//h1[contains(text(), "Авторизация")]')
