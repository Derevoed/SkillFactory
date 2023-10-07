from pages.base import WebPage
from pages.elements import WebElement


"""Страница регистрации"""


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://lk.rt.ru/'
        super().__init__(web_driver, url)

    # Кнопка войти с паролем на стартовой странице
    std_btn = WebElement(id='standard_auth_btn')

    # Строка ссылка перехода на страницу регистрации
    reg_link = WebElement(id='kc-register')

    # Поле ввода "Имя"
    name_field = WebElement(xpath='//input[@name="firstName"]')

    # Поле ввода "Фамилия"
    last_name_field = WebElement(xpath='//input[@name="lastName"]')

    # Поле ввода "E-mail или мобильный телефон"
    email_field = WebElement(id='address')

    # Появляющаяся надпись "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    check_name = WebElement(xpath=
                            '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

    # Появляющаяся надпись "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX,
    # или email в формате example@email.ru"
    check_tel_mail = WebElement(xpath='//span[contains(text(), "Введите телефон в формате +7ХХХХХХХХХХ '
                                      'или +375XXXXXXXXX, или email в формате example@email.ru")]')

    # Поле ввода "Пароль"
    password_field = WebElement(id='password')

    # Поле ввода "Подтверждение пароля"
    confirm_password_field = WebElement(id='password-confirm')

    # Введенный телефон
    inserted_tel = WebElement(xpath='//input[@name="address"]')

    # Кнопка "Зарегистрироваться"
    registration_btn = WebElement(xpath='//button[@name="register"]')

    # Проверка, что учетная запись уже существует. Текст сообщения "Учётная запись уже существует"
    check_user_exist = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div/h2')
