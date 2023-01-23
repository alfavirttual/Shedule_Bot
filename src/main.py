from config import name_users_table, name_schedule_table
from view import View
from controller import Controller
from model import PostgreSQL
from datetime import date, datetime
from bot import Bot




def main():
    bot = Bot().return_bot()
    view = View(bot)
    model = PostgreSQL()
    controller = Controller(model, view, bot)
    controller.hendler()

    print("[INFO] Bot is started")
    bot.infinity_polling()
'''
    __num_week = 1
    __day_week = date.today().isoweekday()
    __time = datetime.now().time()
    __group = None
    __save = False
    button_name = ["I неделя", "II неделя", "На сегодня", "На завтра"]

    @bot.message_handler(commands=['start'])
    def send_message(message):
        view.send_message(message, "Здравствуйте!")
        # проверка есть ли пользователь с таким ник неймом в базе данных
        view.send_message(message, "Для дальнейше работы с ботом необходима регистрация")
        view.send_message(message, "Укажите название группы")

        @bot.message_handler(content_types='text')
        def register(message):
            model.paste(name_users_table, groupp=message.text, user_name=message.from_user.username)
            # проверка есть ли такая группа в бд
            view.send_message(message, "Вы успешно зарегестрированны!")
            text = "Показать рассписание?"
            coord = [2, 2]
            view.create_button(message, button_name, coord, text)
            bot.register_next_step_handler(message, button_handler)

    def button_handler(message):

        if not (message.text in button_name):
            view.send_message(message, "Введён не корректный запрос!")
            view.send_message(message, "Показать рассписание?")
        else:
            __schedule = None
            __num_week = 1
            __day_week = date.today().isoweekday()
            __group = model.select(name_users_table,
                                   "user_name='{0}'".format(message.from_user.username),
                                   "groupp")
            __group = __group[0][0]
            if message.text == "На сегодня":
                __schedule = model.return_schedule(name_schedule_table, __day_week, bool(__num_week), __group)
            elif message.text == "На завтра":
                if __day_week == 7:
                    __day_week = 1
                else:
                    __day_week += 1
                __schedule = model.return_schedule(name_schedule_table, __day_week, bool(__num_week), __group)
            elif message.text == "I неделя":
                __schedule = model.return_schedule(name_schedule_table, 'all', True, __group)
            elif message.text == "I неделя":
                __schedule = model.return_schedule(name_schedule_table, 'all', False, __group)
            view.view_schedule(message, __schedule, message.text, __day_week)
        view.send_message(message, "Показать рассписание?")
        bot.register_next_step_handler(message, button_handler)
'''




if __name__ == '__main__':
    main()
