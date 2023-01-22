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
    __save = False
    button_name = ["I неделя", "II неделя", "На сегодня", "На завтра"]

    @bot.message_handler(commands=['start'])
    def send_message(message):
        view.send_message(message, "Здравствуйте!")
        #проверка есть ли ползователь с таким ник неймом в базе данных
        view.send_message(message, "Для дальнейше работы с ботом необходима регистрация")
        view.send_message(message, "Укажите название группы")
        @bot.message_handler(content_types='text')
        def register(message):
            model.paste("users", groupp=message.text, user_name=message.from_user.username)
            # проверка есть ли такая группа в бд
            view.send_message(message, "Вы успешно зарегестрированны!")
            text = "Показать рассписание?"
            coord = [2, 2]
            view.create_button(message, button_name, coord, text)
            bot.register_next_step_handler(message, button_hendler)



    def button_hendler(message):
        if not (message.text in  button_name):
            text = "Введён не корректный запрос!"
            view.send_message(message, text)
            text = "Показать рассписание?"
            view.send_message(message, text)
        else:
            __schedule = None
            __num_week = 1
            __day_week = date.today().isoweekday()
            __group = model.select("users",
                                   "user_name='{0}'".format(message.from_user.username),
                                   "groupp")
            __group = __group[0][0]
            if message.text == "На сегодня":
                __schedule = model.return_schedule("sсhedule", __day_week, bool(__num_week), __group)
            elif message.text == "На завтра":
                if __day_week == 7: __day_week = 1
                else: __day_week += 1
                __schedule = model.return_schedule("sсhedule", __day_week, bool(__num_week), __group)
            elif message.text == "I неделя":
                __schedule = model.return_schedule("sсhedule", 'all', True, __group)
            elif message.text == "I неделя":
                __schedule = model.return_schedule("sсhedule", 'all', False, __group)
            view.view_schedue(message, __schedule,  message.text, __day_week)
        print('fdfdf')
        bot.register_next_step_handler(message, button_hendler)

    print("[INFO] Bot is started")
    bot.infinity_polling()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
