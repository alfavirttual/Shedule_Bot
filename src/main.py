import telebot
from config import token
from view import View
from controller import Controller
from ..model import PostgreSQL

class Bot:
    __token = None

    def __init__(self, token=token):
        self.__token = token
        self.bot = telebot.TeleBot(token)

    def ret_bot(self):
        return self.bot



def main():
    bot = Bot().ret_bot()
    view = View(bot)
    model = PostgreSQL()
    controller = Controller(model, view)


    @bot.message_handler(commands=['start'])
    def start_bot(message):
        bot.send_message(message.chat.id, 'Привет')

    print("[INFO] Bot is started")
    bot.infinity_polling()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
