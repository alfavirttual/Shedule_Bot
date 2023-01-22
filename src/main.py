import telebot
from config import token
from view import View
from controller import Controller
from model import PostgreSQL
from telebot import types
class Bot:
    __token = None

    def __init__(self, token=token):
        self.__token = token
        self.bot = telebot.TeleBot(token)

    def return_bot(self):
        return self.bot


def main():
    bot = Bot().return_bot()
    view = View(bot)
    model = PostgreSQL()
    controller = Controller(model, view)

    button_name = ['a', 'b', 'c', 'd']
    coord = [2,2]
    text = "repl"
    @bot.message_handler(commands=['start'])
    def send_message(message):
        view.send_message(message, "Привет")
        view.send_message(message, "Укажи имя группы")
        @bot.message_handler(content_types='text')
        def upload_db(message):
            model.paste("tab2", groupp=message.text, user_name=message.from_user.username)


        @bot.message_handler(content_types='text')
        def key_logger(message):
            view.send_message(message, message.text)
            view.create_button(message, button_name, coord, text)


    print("[INFO] Bot is started")
    bot.infinity_polling()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
