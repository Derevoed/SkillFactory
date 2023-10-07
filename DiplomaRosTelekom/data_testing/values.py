"""Тестовые величины/данные используемые при тестировании полей ввода."""


"""Данные для тестирования полей ввода имени и фамилии на странице регистрации (test_reg_page_name_lastname.py)"""

kir_line31 = 'ОРлаомтидвлООвлдвдьййццъхжмбмьа'    # Строка кириллицей в 31 символ

# Строка кириллицей в 255 символов
kir_line255 = 'ПуббиНщмърФЖпаымСмОхлПЬерНБсжТшГюЛкъиВерПхСаубГтеЫХсГмнЙоЛюкхцэыЪнТшэтжсЦРьвПюыРцБЯБХъиЖжАъЛЛЩлЧПЛпют' \
              'ЮСВДрЭПБВЩЯВОьДцбЦъФЗЫсздЦПтишДдсБУлМЕьойдРАЬжМЬЗмМСИЮщндВЬФышшХвйУСЩЗчКГЛФЧТЫЪЯШШЫхинБуХзКеСоАвчЯНъу' \
              'щябюбвыждММЩюПкчШтСрзкХкТЩЫциаУЬМФлиеДЫюДЛВйвЬЮЕцчРцМ'

line31 = 'юеаАk0ЪUJКьqЖUХРz0эЛ5РQМь7НjO0Е'         # Строка в 31 символ

# Строка в 255 символов
line255 = 'bДу5Ibе8ЯСы6рdСсe3ФwАсLMCQЕBо8vVК8ЦСЖэIЦсыFъСЪ0ЪP5ИEYРЯГЛРЪXjЦъИМDWфИTgiCpйdАsдшеoЖ9aЩо92с1ПHJыWchЛOяЖрm' \
          'MykxaЗfОAшoЮИз8IMРEeЮвf6жрmQTlMfO7АJВчУlНэАФЙЮfйМ6qUтFН7GkКЕъСpvdFЛeЧзAпSПgюыКЖхсmзXPyйЛДЖRxojЩМиWЫNъГеqc' \
          'qвфxБLRВГЖыrqцыЩ6ЪзIжiHСJЕpОJwCJeяKHstс4МУuхтh'

kir_line10 = 'йЗтбвдТуДц'                               # Строка кириллицей в 10 символов
kir_line10_dash = 'йЗтб-дТуДц'                          # Строка кириллицей в 10 символов со знаком тире (-)
kir_line29 = 'ЛПыЫдеЙжЭНКзУьбЦЫоуаэоунИэщКЙ'            # Строка кириллицей в 29 символов
kir_line29_dash = 'Щщгвщащуэррвщъ-Уидфввэжвпшнве'       # Строка кириллицей в 29 символов со знаком тире (-)
kir_line30 = 'щЩгвЩАЩуэРРВЩЪУИчДФВВЭЖвПшНвЕф'           # Строка кириллицей в 30 символов
kir_line30_dash = 'Щщгвщащуэррвщъ-Уидфввэжвпшнвеф'      # Строка кириллицей в 30 символов со знаком тире (-)
line_4_16 = 'Щщаг-Щъуидфаввэжвпшнв'                     # Строка кириллицей из 4 и 16 символов через тире (-)
line_16_4 = 'Щъуидфввэжвпшнве-Вввв'                     # Строка кириллицей из 16 и 4 символов через тире (-)


"""Данные для тестирования поля ввода телефона на страницах: 
регистрации (test_reg_page_tel_and_email.py)
авторизации (test_auth_page_tel.py)"""

# Для негативных проверок
tel_10_num = '+7900800706'      # Телефон - 10 цифр
tel_4_num = '+7901'             # Телефон - 4 цифры
tel_12_num = '+790080070605'    # Телефон - 12 цифр
tel_11_num = '+37533445555'     # Телефон - 11 цифр начинающийся с +375
tel_13_num = '+3753344555545'   # Телефон - 13 цифр начинающийся с +375
tel_1_num = '8'                 # Телефон - 1 цифра

# Для позитивных проверок автозамены
tel_pos_1 = '89008007060'
tel_pos_2 = '+89008007060'
tel_pos_3 = '8-900-800-70-60'
tel_pos_4 = '8 900 800 70 60'
tel_pos_5 = '8 9 0 0 8 0 0 7 0 6 0'
tel_pos_6 = '8-9-0-0-8-0-0-7-0-6-0'
tel_pos_7 = '375900800763'
tel_pos_8 = '375 900 800 763'
tel_pos_9 = ' 3 7 5-900-8007 63'

reference_number_1 = '79008007060'     # Первый эталонный номер телефона для сравнения в результатах тестов
reference_number_2 = '375900800763'    # Второй эталонный номер телефона для сравнения в результатах тестов


"""Данные для тестирования поля ввода E-mail на странице регистрации (test_reg_page_tel_and_email.py)"""

# Для негативных проверок
email_neg_1 = 'test@mailru'      # Email без точек в доменной части
email_neg_2 = 'testmail.ru'      # Email без @
email_neg_3 = '.test@mail.ru'    # Email начинающийся с точки
email_neg_4 = 'te st@mail.ru'    # Email с пробелами в имени аккаунта
email_neg_5 = 'test@ma il.ru'    # Email с пробелами в доменной части
email_neg_6 = '@mail.ru'         # Email без имени аккаунта
email_neg_7 = 'test@.ru'         # Email без доменной части

# Email длинной > 320 символов
email_neg_8 = 'Vdpww43qhnQnftykMVRa804j9I51Yv45Nng2Qwcc3IJpqicYuZYR7krFoomwfNSZDGpE6haRXCoDewhTTtrIIoDY8vvRcK6Ajp5B' \
              'bcDu3UqYBJTfKxpQfsKw5Oc8KtIjUAPO138gD4viARw6NOcbk3aoUtzqMDudfvFyJhtmUPpw7dKlJhbqBr3n6Scp6L4GjJtmaTFz' \
              'nnbroH6KJhQgstKTKWshsnZotHvU5H2UctHKjMtxTt3nkVLRDYGsXDMXNJqZMGtaeEKgpwKOYO0YUynAXWQIXyXVLrmy8i1iHxTD' \
              'XryA9LTk6lr6MtYfp6q8@mail.ru'
email_neg_9 = 'Vdp@ww43qhnQnftykMVRa804j9I51Yv45Nng2Qwcc3IJpqicYuZYR7krFoomwfNSZDGpE6haRXCoDewhTTtrIIoDY8vvRcK6Ajp5' \
              'BbcDu3UqYBJTfKxpQfsKw5Oc8KtIjUAPO138gD4viARw6NOcbk3aoUtzqMDudfvFyJhtmUPpw7dKlJhbqBr3n6Scp6L4GjJtmaT' \
              'FznnbroH6KJhQgstKTKWshsnZotHvU5H2UctHKjMtxTt3nkVLRDYGsXDMXNJqZMGtaeEKgpwKOYO0YUynAXWQIXyXVLrmy8i1iH' \
              'xTDXryA9LTk6lr6MtYfp6q8mail.ru'

# Для позитивных проверок
email_pos_1 = 'tes1t@mail.ru'      # Email с цифрами в имени аккаунта
email_pos_2 = 'test@ma12il.ru'     # Email с цифрами в доменной части
email_pos_3 = 'te-st@mail.ru'      # Email с дефисом в имени аккаунта
email_pos_4 = 'test@ma-il.ru'      # Email с дефисом в доменной части
email_pos_5 = 't_est@mail.ru'      # Email со знаком подчеркивания в имени аккаунта
email_pos_6 = 'test@ma_il.ru'      # Email со знаком подчеркивания в доменной части
email_pos_7 = 't.e.s.t@mail.ru'    # Email с точками в имени аккаунта
email_pos_8 = 'test@m.a.i.l.ru'    # Email с точками в имени аккаунта
