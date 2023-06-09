import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы выполнить перевод валют необходимо ввести команды боту в следующем формате:\n<название валюты, которую хотите конвертировать>\
<в какую валюту перевести> <количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты для перевода: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise ConvertionException('Необходимо ввести три параметра: валюта-1, валюта-2, количество переводимой валюты.')

        base, quote, amount = values
        total_quote = CurrencyConverter.get_price(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Конвертация {base} в {quote} : {amount} {base} = {total_quote} {quote}.'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)