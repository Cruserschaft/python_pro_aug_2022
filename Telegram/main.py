import telebot
import config
from telebot import types
import group
import token_val

bot = telebot.TeleBot(token_val.TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(config.ENTER_GROUP)
    item2 = types.KeyboardButton(config.CREATE_GROUP)
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == config.ENTER_GROUP:
        pass
    elif message.text == config.CREATE_GROUP:
        bot.send_message(message.chat.id, "Группа создана, добавьте друзей с помощью следующего личного идентификатора и войдите сами")
        bot.send_message(message.chat.id, group.create_group(message.chat.id))


bot.polling(none_stop=True)
