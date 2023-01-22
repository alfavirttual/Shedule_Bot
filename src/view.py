from telebot import types
import numpy as np
import emoji


class View():

    def __init__(self, bot):
        self.bot = bot

    def send_message(self, message, text):
        self.bot.send_message(message.chat.id, text)

    def create_button(self, message, button_name, coord, text):
        __markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        __button = []
        for i in range(len(button_name)):
            __button.append(types.KeyboardButton(button_name[i]))
        __button = np.reshape(button_name, coord)

        for i in range(coord[0]):
            __markup.row(*__button[i])
        self.bot.send_message(message.from_user.id, text, reply_markup=__markup)

    def view_schedue(self, message, schedule, key):
        __mass = []
        __weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
                    'Пятница', 'Суббота', 'Воскресенье']

        if key == "I неделя":
            key = "Рассписание на I неделю:"
        elif key == "II неделя":
            key = "Рассписание на II неделю:"
        elif key == "На сегодня":
            key = "Рассписание на сегодня:"
        elif key == "На завтра":
            key = "Рассписание на завтра:"
        self.bot.send_message(message.from_user.id, key)
        print(schedule)
        print(len(schedule))
        print(len(schedule[0]))
        for i in range(len(schedule)):
            __mass.append(emoji.emojize(':green_circle:'))
            __mass.append('\t')
            __mass.append(__weekdays[i])
            __mass.append('\n'+'\n')
            print(i)
            for j in range(len(schedule[0][i])):
                print(j)
                __mass.append(emoji.emojize(':books:'))
                __mass.append('\t')
                __mass.append(schedule[i][1][j])
                __mass.append('\n')
                __mass.append(emoji.emojize(':alarm_clock:'))
                __mass.append('\t')
                __mass.append(schedule[i][0][j])
                __mass.append('\n')
                __mass.append(emoji.emojize(':door:'))
                __mass.append('\t')
                __mass.append(schedule[i][2][j])
                __mass.append('\n')
                __mass.append(emoji.emojize(':man_teacher:'))
                __mass.append('\t')
                __mass.append(schedule[i][3][j])
                __mass.append('\n')
                __mass.append('\n')

            self.bot.send_message(message.from_user.id, ''.join(map(str, __mass)))
