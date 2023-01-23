from telebot import types
import numpy as np
import emoji


class View:

    __markup = None
    __button = None
    __weekdays = None
    __mass = None

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

    def view_schedule(self, message, schedule, key, day_week):

        __weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
                      'Пятница', 'Суббота', 'Воскресенье']

        if key == "I неделя":
            key = "Рассписание на I неделю:"
        elif key == "II неделя":
            key = "Рассписание на II неделю:"
        elif key == "На сегодня":
            key = "Рассписание на сегодня:"
            __weekdays = [__weekdays[day_week - 1]]
        elif key == "На завтра":
            key = "Рассписание на завтра:"
            __weekdays = [__weekdays[day_week - 1]]

        self.bot.send_message(message.from_user.id, key)
        for i in range(len(schedule)):
            __mass = [emoji.emojize(':green_circle:'), '\t', __weekdays[i], '\n' + '\n']
            for j in range(len(schedule[i][0])):
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
