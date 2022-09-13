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


register_group = False
@bot.message_handler(content_types=["text"])
def main(message):
    global register_group
    if message.text == config.ENTER_GROUP:
        pass



    elif message.text == config.CREATE_GROUP or register_group:
        if group.sq_search(message.chat.id):
            bot.send_message(message.chat.id, "Вы уже состоите в группе")
            return

        if not register_group:
            bot.send_message(message.chat.id, "Введите своё имя", reply_markup=None)
            register_group = True
            return

        bot.send_message(message.chat.id, "Проходит регистрация, подождите...")
        bot.send_message(message.chat.id, group.create_group(message.chat.id, message.text))
        register_group = False





bot.polling(none_stop=True)
