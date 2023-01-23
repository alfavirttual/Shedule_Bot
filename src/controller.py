from datetime import date, datetime
from config import name_users_table, name_schedule_table


class Controller:
    "Класс - обрботчик запросов пользователя"

    __num_week = None
    __day_week = None
    __group = None

    def __init__(self, model, view, bot):
        self.model = model
        self.view = view
        self.bot = bot

    def hendler(self):
        button_name = ["I неделя", "II неделя", "На сегодня", "На завтра"]
        @self.bot.message_handler(commands=['start'])
        def send_message(message):
            self.view.send_message(message, "Здравствуйте!")
            # проверка есть ли пользователь с таким ник неймом в базе данных
            self.view.send_message(message, "Для дальнейше работы с ботом необходима регистрация")
            self.view.send_message(message, "Укажите название группы")

            @self.bot.message_handler(content_types='text')
            def register(message):
                self.model.paste(name_users_table, groupp=message.text, user_name=message.from_user.username)
                # проверка есть ли такая группа в бд
                self.view.send_message(message, "Вы успешно зарегестрированны!")
                text = "Показать рассписание?"
                coord = [2, 2]
                self.view.create_button(message, button_name, coord, text)
                self.bot.register_next_step_handler(message, button_handler)


        def button_handler(message):

            if not (message.text in button_name):
                self.view.send_message(message, "Введён не корректный запрос!")
                self.view.send_message(message, "Показать рассписание?")
            else:
                __schedule = None
                __num_week = 1
                __day_week = date.today().isoweekday()
                __group = self.model.select(name_users_table,
                                       "user_name='{0}'".format(message.from_user.username),
                                       "groupp")
                __group = __group[0][0]
                if message.text == "На сегодня":
                    __schedule = self.model.return_schedule(name_schedule_table, __day_week, bool(__num_week), __group)
                elif message.text == "На завтра":
                    if __day_week == 7:
                        __day_week = 1
                    else:
                        __day_week += 1
                    __schedule = self.model.return_schedule(name_schedule_table, __day_week, bool(__num_week), __group)
                elif message.text == "I неделя":
                    __schedule = self.model.return_schedule(name_schedule_table, 'all', True, __group)
                elif message.text == "I неделя":
                    __schedule = self.model.return_schedule(name_schedule_table, 'all', False, __group)
                self.view.view_schedule(message, __schedule, message.text, __day_week)
            self.view.send_message(message, "Показать рассписание?")
            self.bot.register_next_step_handler(message, button_handler)










