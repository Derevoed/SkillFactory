import os.path

from api import PetFriends
from settings import valid_email, valid_password, invalid_auth_key, invalid_email, invalid_password
from settings import name255, animal_type255


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key."""

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter='my_pets'):
    """Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='p4elka', animal_type='bee', age='1', pet_photo='images/bzz.jpeg'):
    """Проверяем, что можно добавить питомца с корректными данными."""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_successful_update_pet_information(name='Жужило', animal_type='пчела', age='3'):
    """Проверяем возможность обновления информации о питомце."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_information_about_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # Если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception('У меня нет питомцев')


def test_successful_delete_pet():
    """Проверяем возможность удаления питомца."""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'SuperBee', 'bee', '1', 'images/bzz.jpeg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Запрашиваем список своих питомцев и проверяем, что статус ответа равен 200 и в списке питомцев
    # нет id удалённого питомца
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    assert status == 200
    assert pet_id not in my_pets.values()


def test_add_new_pet_without_photo(name='Shrek', animal_type='ogr', age='25'):
    """Проверяем возможность добавления нового питомца без фотографии."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_photo_for_pet(pet_photo='images/shrek.jpg'):
    """Проверяем возможность добавления фотографии к ранее созданному питомцу."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем, если список питомцев не пустой, то добавляем фотографию к ранее созданному питомцу
    if len(my_pets) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result['pet_photo'] != ''
    else:
        # Если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception('У меня нет питомцев')


def test_unsuccessful_add_new_pet_with_negative_age(name='NegativeBee', animal_type='minus', age='-1',
                                                    pet_photo='images/bzz.jpeg'):
    """Проверяем невозможность добавления нового питомца с отрицательным возрастом."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Пробуем добавить питомца с отрицательным возрастом, при неудачном добавлении должны получить ответ со статусом 400
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['name'] != name


def test_unsuccessful_delete_pet_with_invalid_auth_key():
    """Проверяем невозможность удаления питомца с недействительным ключом авторизации."""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets) == 0:
        pf.add_new_pet(auth_key, 'SuperBee', 'bee', '1', 'images/bzz.jpeg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Берём id первого питомца из списка, присваиваем auth_key значение недействительного ключа
    # и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    auth_key = invalid_auth_key
    status = pf.delete_pet(auth_key, pet_id)

    # При невозможности удаления питомца с не действительным ключом должны получить ответ со статусом 403
    assert status[0] == 403


def test_unsuccessful_add_new_pet_with_invalid_auth_key(name='p4el', animal_type='bee', age='2',
                                                        pet_photo='images/bzz.jpeg'):
    """Проверяем невозможность добавления нового питомца с недействительным ключом авторизации."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # присваиваем auth_key значение недействительного ключа и пробуем добавить нового питомца
    auth_key = invalid_auth_key
    status, _ = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # При невозможности добавления питомца с не действительным ключом должны получить ответ со статусом 403
    assert status == 403


def test_unsuccessful_add_new_pet_with_empty_fields(name='', animal_type='', age=''):
    """Проверяем невозможность добавления нового питомца с пустыми полями."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # При неудачном добавлении должны получить ответ со статусом 400
    assert status == 400


def test_unsuccessful_get_api_key_with_invalid_data(email=invalid_email, password=invalid_password):
    """Проверяем невозможность получения ключа авторизации при отправке недействительных значений email и password."""

    status, _ = pf.get_api_key(email, password)

    # При запросе api_key с недействительными email и password должны получить ответ со статусом 403
    assert status == 403


def test_unsuccessful_add_new_pet_with_letter_in_age(name='Shrek', animal_type='ogr', age='two'):
    """Проверяем невозможность добавления нового питомца с буквенным значением в поле возраст"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # При неудачном добавлении питомца должны получить ответ со статусом 400
    assert status == 400


def test_unsuccessful_add_new_pet_with_255_symbols_in_field(name=name255, animal_type=animal_type255, age='1'):
    """Проверяем невозможность добавления нового питомца с передачей в параметрах name и animal_type строк длинной
    255 элементов с содержанием букв и цифр"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # При неудачном добавлении питомца должны получить ответ со статусом 400
    assert status == 400


def test_unsuccessful_update_pet_info_with_incorrect_data(name='☺☻♥♦酒家', animal_type='原千五♥♦♣♠•◘', age='1000000'):
    """Проверяем невозможность обновления данных питомца: имя, тип, возраст на данные с использованием символов
    альтернативной клавиатуры, японского и китайского письма, с передачей возраста большого числового значения"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем, если список питомцев не пустой, то пробуем обновить данные ранее созданного питомца
    if len(my_pets['pets']) > 0:
        status, result = pf.update_information_about_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Невозможность обновления подтверждается ответом со статусом 400
        assert status == 400
    else:
        raise Exception('У меня нет питомцев')


def test_successful_update_pet_photo(pet_photo='images/replacing_picture.jpg'):
    """Проверяем возможность обновить фотографию питомца у которого уже есть фотография"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Если список питомцев не пустой и у питомца с нулевой позицией есть фотография
    if len(my_pets) > 0 and my_pets['pets'][0]['pet_photo'] != '':

        # Присваиваем значение текущей фотографии к параметру old_photo
        old_photo = my_pets['pets'][0]['pet_photo']

        # Пробуем поменять фотографию питомца на новую с получением статуса с кодом 200
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200

        # Проверяем, что новая фотография отличается от старой
        assert result['pet_photo'] != old_photo

    # Если список питомцев не пустой и у питомца с нулевой позицией нет фотографии
    elif len(my_pets) > 0 and my_pets['pets'][0]['pet_photo'] == '':

        # Добавляем фотографию питомцу
        _, _ = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo='images/shrek.jpg')

        # Присваиваем значение текущей фотографии к параметру old_photo
        old_photo = my_pets['pets'][0]['pet_photo']

        # Пробуем поменять фотографию питомца на новую с получением статуса с кодом 200
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200

        # Проверяем, что новая фотография отличается от старой
        assert result['pet_photo'] != old_photo
    else:
        # Если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception('У меня нет питомцев')
