import telebot
from config import token
from view import View
from controller import Controller
from model import PostgreSQL
from datetime import date, datetime
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

    __num_week = 1
    __day_week = date.today().isoweekday()
    __time = datetime.now().time()
    __group = None
    button_name = ["I неделя", "II неделя", "На сегодня", "На завтра"]

    @bot.message_handler(commands=['start'])
    def send_message(message):
        view.send_message(message, "Здравствуйте!")
        view.send_message(message, "Укажи имя группы")
        upload_user_db(message)

    def upload_user_db(message):
        model.paste("users", groupp=message.text, user_name=message.from_user.username)
        text = "Показать рассписание?"
        coord = [2,2]
        view.create_button(message, button_name, coord, text)



    @bot.message_handler(content_types='text')
    def button(message):
        print(2)
        print(message.text)
        if not (message.text in  button_name):
            text = "Введите корректный запрос!"
            view.send_message(message, text)
            text = "Показать рассписание?"
            view.send_message(message, text)
            button(message,  button_name)
        else:
            __schedule = None
            __num_week = 1
            __day_week = date.today().isoweekday()
            __group = model.select("users",
                                   "username={0}".format(message.from_user.username),
                                   "group")
            if message.text == "На сегодня":
                __schedule = model.return_schedule("sсhedule", __day_week, bool(__num_week), __group)
            elif message.text == "На завтра":
                if __day_week == 7: __day_week = 1
                __schedule = model.return_schedule("sсhedule", __day_week, bool(__num_week), __group)
            elif message.text == "I неделя":
                __schedule = model.return_schedule("sсhedule", 'all', True, __group)
            elif message.text == "I неделя":
                __schedule = model.return_schedule("sсhedule", 'all', False, __group)
            view.view_schedue(message, __schedule,  button_name)


    print("[INFO] Bot is started")
    bot.infinity_polling()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
