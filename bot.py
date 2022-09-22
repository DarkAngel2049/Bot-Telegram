import telebot
from telebot import types

import config

BOT_TOKEN = "1797521903:AAEq2ssv3IbfWkD0MeUkumqiIT55NuNsRsw"
bot = telebot.TeleBot(config.BOT_TOKEN)
types.InlineKeyboardButton(text="Текст кнопки",
                           callback_data="Ответ которая вернет кнопка(будет нужен дальше, запомните про него)")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Создать пароль", callback_data="start")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id,
                     'Привет! Я бот который поможет тебе придумать пароли\nДля начала нажми на кнопку ниже',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "start":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Простой', callback_data='pwd1')
        btn2 = types.InlineKeyboardButton('Средний', callback_data='pwd2')
        btn3 = types.InlineKeyboardButton('Сложный', callback_data='pwd3')
        keyboard.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="️Выбери сложность пароля️", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "start":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Простой', callback_data='pwd1')
        btn2 = types.InlineKeyboardButton('Средний', callback_data='pwd2')
        btn3 = types.InlineKeyboardButton('Сложный', callback_data='pwd3')
        keyboard.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="️Выбери сложность пароля️", reply_markup=keyboard)


pwd_length = 10
if call.data == "pwd1":
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перегенирировать', callback_data='pwd1')
    btn2 = types.InlineKeyboardButton('Вернутся в начало', callback_data='start')
    keyboard.add(btn1)
    keyboard.add(btn2)
    pwd = password_generate.easy_pass(config.pwd_length)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Твой пароль - `{0}`".format(pwd), reply_markup=keyboard, parse_mode='Markdown')

if call.data == "pwd2":
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перегенирировать', callback_data='pwd2')
    btn2 = types.InlineKeyboardButton('Вернутся в начало', callback_data='start')
    keyboard.add(btn1)
    keyboard.add(btn2)
    pwd = password_generate.medium_pass(config.pwd_length)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Твой пароль - `{0}`".format(pwd), reply_markup=keyboard, parse_mode='Markdown')

if call.data == "pwd3":
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перегенирировать', callback_data='pwd3')
    btn2 = types.InlineKeyboardButton('Вернутся в начало', callback_data='start')
    keyboard.add(btn1)
    keyboard.add(btn2)
    pwd = password_generate.hard_pass(config.pwd_length)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Твой пароль - `{0}`".format(pwd), reply_markup=keyboard, parse_mode='Markdown')

if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True, interval=2)
