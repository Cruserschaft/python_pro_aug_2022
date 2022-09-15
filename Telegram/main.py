import telebot
import config
from telebot import types
import group
import token_val
from flask import Flask, request
import os


app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=["start"])
def start(message):
    if group.sq_search(message.chat.id):
        bot.send_message(message.chat.id, "Вы уже состоите в группе")
        return
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(config.ENTER_GROUP)
    item2 = types.KeyboardButton(config.CREATE_GROUP)
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)


@bot.message_handler(commands=['clear'])
def clear(message):
    tmp = message.id - 1
    tmp2 = message.chat.id
    stop = 0
    while tmp > 0:
        try:
            print(tmp)
            bot.delete_message(message.chat.id, tmp)
            stop = 0
        except:
            if stop > 20:
                break
            stop += 1
        finally:
            tmp -= 1


@bot.message_handler(commands=['exit'])
def leave_group(message):
    if not group.sq_search(message.chat.id):
        bot.send_message(message.chat.id, "Вы не состоите в группе")
        return
    group.sq_remove(message.chat.id)
    bot.send_message(message.chat.id, "Вы удалены из группы")


@bot.message_handler(commands=['help'])
def docs(message):
    tmp = """
/start - Начало
/clear - Очистить
/id - Просмотреть ID группы
/exit - Выйти из группы
    """
    bot.send_message(message.chat.id, tmp)


@bot.message_handler(commands=['id'])
def id_group(message):
    if not group.sq_search(message.chat.id):
        bot.send_message(message.chat.id, "Вы не состоите в группе")
        return

    tmp = group.sq_search(message.chat.id, ret_id_group=True)

    bot.send_message(message.chat.id, "ID вашей группы")
    bot.send_message(message.chat.id, tmp)


register_group = False
enter_group = False
enter_group_name = False
tmp_grp_id = None


@bot.message_handler(content_types=["text"])
def main(message):
    global register_group
    global enter_group
    global enter_group_name
    global tmp_grp_id
    if group.sq_search(message.chat.id):
        tmp = group.sq_search(message.chat.id, ret_users=True)
        tmp.pop(tmp.index(message.chat.id))
        print(message.id)
        for i in tmp:
            try:
                bot.send_message(i, message.text)
            except:
                pass

    if message.text == config.ENTER_GROUP or enter_group or enter_group_name:
        if group.sq_search(message.chat.id):
            bot.send_message(message.chat.id, "Вы уже состоите в группе")
            return

        if not enter_group and not enter_group_name:
            bot.send_message(message.chat.id, "Введите ID группы")
            enter_group = True
            return

        if enter_group:
            print("enter_group")
            print(group.sq_search_by_grp_id(message.text))
            if not group.sq_search_by_grp_id(message.text):
                bot.send_message(message.chat.id, "Не найдена группа")
                enter_group = False
                return
            tmp_grp_id = message.text
            bot.send_message(message.chat.id, "Введите имя")
            enter_group = False
            enter_group_name = True
            return

        if enter_group_name:
            print("enter_group_name")
            group.register_user(message.chat.id, tmp_grp_id, message.text)
            enter_group_name = False
            bot.send_message(message.chat.id, "Вы зарегестрированы, введите /clear для очистки")

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


@app.route("/" + str(TOKEN), methods=["POST"])
def get_message():
    bot.process_new_messages([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200


@app.route("/")
def main():
    bot.remove_webhook()
    bot.set_webhook(url="https://poshli-kurit-bot.herokuapp.com/"+TOKEN)
    return "Python Telegram Bot", 200


if __name__ == "main":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))