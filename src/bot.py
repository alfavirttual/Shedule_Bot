import telebot;

bot = telebot.TeleBot('1288987415:AAFkTpWoqYqXJ9yMpuqWSXqsjrGaW1fm24k');
from telebot import types
from datetime import date
import emoji
import copy
import json

week_now = 1
data_enter = []
day = 0
data_now = date(2020, 1, 1)
time_one = [[1], [1], [1], [1], [1, 2, 3], [2, 3, 1], [1, 2, 4]]
time_two = [[1], [1], [1], [1], [1, 2, 3], [2, 3, 1], [1, 2, 4]]
ticher_one = [[1], [1], [1], [1], [11, 22, 33], [22, 33, 11], [1, 7, 8]]
ticher_two = [[1], [1], [1], [1], [11, 22, 33], [22, 33, 11], [1, 7, 8]]
discipline_one = [[1], [1], [1], [1], [4, 5, 6], [7, 8, 9], [1, 9, 0]]
discipline_two = [[1], [1], [1], [1], [4, 5, 6], [7, 8, 9], [1, 9, 0]]

weekdays = ['Абсолютный_ноль', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
time_arr = ["Спи сколько хочешь )", "8:30 - 10:00", "10:10 - 11:40", "11:50 - 13:20", "13:40 - 15:10", "15:20 - 16:50",
            "17:00 - 18:30", "18:35 - 21:30"]

day_discipline = []
day_time = []
day_ticher = []


def shedule_write():
    file = 'data.json'

    global week_now
    global data_enter
    global time_one
    global time_two
    global ticher_one
    global ticher_two
    global discipline_one
    global discipline_two

    shedule = {
        "week_now": week_now,
        "data_enter": data_enter,
        "time_one": time_one,
        "time_two": time_two,
        "ticher_one": ticher_one,
        "ticher_two": ticher_two,
        "discipline_one": discipline_one,
        "discipline_two": discipline_two,
    }

    with open(file, 'w') as f:
        json.dump(shedule, f)

    return


def shedule_read():
    file = 'data.json'

    global week_now
    global data_enter
    global time_one
    global time_two
    global ticher_one
    global ticher_two
    global discipline_one
    global discipline_two

    try:
        with open(file) as f:
            shedule = json.load(f)
    except:
        @bot.message_handler(content_types=["text"])
        def text(message):
            bot.send_message(message.from_user.id, "Рассписание не заполнено (")
            print("Расписание не заполнено")
            return
    else:
        week_now = shedule["week_now"]
        data_enter = shedule["data_enter"]
        time_one = shedule["time_one"]
        time_two = shedule["time_two"]
        ticher_one = shedule["ticher_one"]
        ticher_two = shedule["ticher_two"]
        discipline_one = shedule["discipline_one"]
        discipline_two = shedule["discipline_two"]
        return
        print("Расписание загруженно")
    return


def beginning(message):
    shedule_read()

    global day_week
    global week_now
    global data_now

    day_week = date.today().weekday()

    if day_week == 0 and (data_enter[0] != int(date.today().day)) and data_enter[1] != int(date.today().month) and (
            data_now != date.today()):
        data_now = date.today()

        if week_now == 1:
            week_now = 2
        else:
            week_now = 1

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    one = types.KeyboardButton('I неделя')
    two = types.KeyboardButton('II неделя')
    today = types.KeyboardButton('На сегодня')
    tomorrow = types.KeyboardButton('На завтра')
    markup.row(one, two)
    markup.row(today, tomorrow)

    msg = bot.send_message(message.from_user.id, "Показать расписание ?", reply_markup=markup)
    bot.register_next_step_handler(msg, demonstration)


def demonstration(message):
    global day_week
    global ticher_one
    global discipline_one
    global time_one
    global ticher_two
    global discipline_two
    global time_two
    global time_arr

    time_one_one = copy.deepcopy(time_one)
    time_two_two = copy.deepcopy(time_two)

    i = 0
    while i < 6:
        j = 0
        length = len(time_one[i])
        while j < length:
            m = int(time_one[i][j])
            time_one_one[i][j] = time_arr[m]
            j = j + 1
        i = i + 1

    i = 0
    while i < 6:
        j = 0
        length = len(time_two[i])
        while j < length:
            m = int(time_two[i][j])
            time_two_two[i][j] = time_arr[m]
            j = j + 1
        i = i + 1

    if message.text == 'На сегодня' and week_now == 1:

        bot.send_message(message.from_user.id, 'Сегодня у вас:')

        print(str(day_week))

        if day_week == 6:

            bot.send_message(message.from_user.id, "Воскресенье - выходной ")
            beginning(message)
        else:

            length = len(time_one[day_week])
            k = 0
            discipline_now = []
            while k < length:
                discipline_now.append(emoji.emojize(':books:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(discipline_one[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':alarm_clock:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(time_one_one[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':door:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(ticher_one[day_week][k])
                discipline_now.append('\n')
                discipline_now.append('\n')
                k = k + 1

            bot.send_message(message.from_user.id, ''.join(map(str, discipline_now)))
            beginning(message)

    elif message.text == 'На сегодня' and week_now == 2:
        bot.send_message(message.from_user.id, 'Сегодня у вас:')

        if day_week == 6:

            bot.send_message(message.from_user.id, "Воскресенье - выходной ")
            beginning(message)
        else:

            length = len(time_two[day_week])
            k = 0
            discipline_now = []
            while k < length:
                discipline_now.append(emoji.emojize(':books:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(discipline_two[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':alarm_clock:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(time_two_two[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':door:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(ticher_two[day_week][k])
                discipline_now.append('\n')
                discipline_now.append('\n')
                k = k + 1

            bot.send_message(message.from_user.id, ''.join(map(str, discipline_now)))
            beginning(message)

    if message.text == 'На завтра' and week_now == 1:
        bot.send_message(message.from_user.id, 'Завтра у вас:')

        if day_week == 5:
            bot.send_message(message.from_user.id, "Воскресенье - выходной ")
            beginning(message)
        else:

            if day_week == 6:
                day_week = 0
            else:
                day_week = day_week + 1

            length = len(time_one[day_week])
            k = 0
            discipline_now = []
            while k < length:
                discipline_now.append(emoji.emojize(':books:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(discipline_one[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':alarm_clock:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(time_one_one[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':door:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(ticher_one[day_week][k])
                discipline_now.append('\n')
                discipline_now.append('\n')
                k = k + 1

            bot.send_message(message.from_user.id, ''.join(map(str, discipline_now)))
            beginning(message)

    elif message.text == 'На завтра' and week_now == 2:
        bot.send_message(message.from_user.id, 'Завтра у вас:')

        if day_week == 5:
            bot.send_message(message.from_user.id, "Воскресенье - выходной ")
            beginning(message)
        else:

            if day_week == 6:
                day_week = 0
            else:
                day_week = day_week + 1

            length = len(time_two[day_week])
            k = 0
            discipline_now = []
            while k < length:
                discipline_now.append(emoji.emojize(':books:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(discipline_two[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':alarm_clock:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(time_two_two[day_week][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':door:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(ticher_two[day_week][k])
                discipline_now.append('\n')
                discipline_now.append('\n')
                k = k + 1

            bot.send_message(message.from_user.id, ''.join(map(str, discipline_now)))
            beginning(message)

    if message.text == 'I неделя':

        bot.send_message(message.from_user.id, 'Расписание на I неделю:')
        c = 0

        while c < 6:
            discipline_now = []
            length = len(time_one[c])
            k = 0
            discipline_now.append(emoji.emojize(':green_circle:', use_aliases=True))
            discipline_now.append('\t')
            discipline_now.append(weekdays[c + 1])
            discipline_now.append('\n')
            while k < length:
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':books:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(discipline_one[c][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':alarm_clock:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(time_one_one[c][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':door:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(ticher_one[c][k])
                discipline_now.append('\n')
                discipline_now.append('\n')
                k = k + 1

            bot.send_message(message.from_user.id, ''.join(map(str, discipline_now)))
            c = c + 1

        beginning(message)

    if message.text == 'II неделя':

        bot.send_message(message.from_user.id, 'Расписание на II неделю:')
        c = 0

        while c < 6:
            discipline_now = []
            length = len(time_two[c])
            k = 0
            discipline_now.append(emoji.emojize(':green_circle:', use_aliases=True))
            discipline_now.append('\t')
            discipline_now.append(weekdays[c + 1])
            discipline_now.append('\n')
            while k < length:
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':books:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(discipline_two[c][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':alarm_clock:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(time_two_two[c][k])
                discipline_now.append('\n')
                discipline_now.append(emoji.emojize(':door:', use_aliases=True))
                discipline_now.append('\t')
                discipline_now.append(ticher_two[c][k])
                discipline_now.append('\n')
                discipline_now.append('\n')
                k = k + 1

            bot.send_message(message.from_user.id, ''.join(map(str, discipline_now)))
            c = c + 1

        beginning(message)


def pio_1(message):
    global day
    global step

    global ticher_one
    global discipline_one
    global time_one

    global day_discipline
    global day_time
    global day_ticher

    def name(message):
        day_ticher.append(message.text)
        msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:")

        bot.register_next_step_handler(msg, discipline)

    def time(message):
        if message.text.isdigit() == True:
            if int(message.text) >= 1 and int(message.text) <= 7:
                day_time.append(message.text)
                msg = bot.send_message(message.from_user.id, "Введите номер аудитории:")
                bot.register_next_step_handler(msg, name)
            else:
                msg = bot.send_message(message.from_user.id,
                                       "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                bot.register_next_step_handler(msg, time)
        else:
            msg = bot.send_message(message.from_user.id, "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
            bot.register_next_step_handler(msg, time)

    def discipline(message):
        global day
        global step

        global ticher_one
        global discipline_one
        global time_one

        global day_discipline
        global day_time
        global day_ticher

        if message.text == "Следующий день":

            day = day + 1

            if day == 7 and step == 1:
                msg = "Заполнение второй недели."
                choice(message, msg)
                pio_2(message)
            elif day == 14:
                weeks(message)

            else:

                discipline_one.append(day_discipline)
                time_one.append(day_time)
                ticher_one.append(day_ticher)

                day_discipline = []
                day_time = []
                day_ticher = []

                msg = bot.send_message(message.from_user.id, "Ввведите название первого предмета:")
                bot.register_next_step_handler(msg, discipline)


        elif message.text == "Выходной":
            day = day + 1
            if day == 7 and step == 1:
                msg = "Заполнение второй недели."
                choice(message, msg)
                pio_2(message)
            elif day == 14:
                weeks(message)

            else:
                day_discipline.append("Пар нет, кайфуем")
                day_time.append("0")
                day_ticher.append("NAN")
                discipline_one.append(day_discipline)
                time_one.append(day_time)
                ticher_one.append(day_ticher)
                day_discipline = []
                day_time = []
                day_ticher = []
                msg = bot.send_message(message.from_user.id, "Ввведите название первого предмета:")
                bot.register_next_step_handler(msg, discipline)

        else:

            day_discipline.append(message.text)
            msg = bot.send_message(message.from_user.id, "Введите время:")
            bot.register_next_step_handler(msg, time)

    msg = bot.send_message(message.from_user.id, "Введите название предмета:")
    bot.register_next_step_handler(msg, discipline)


def pio_2(message):
    global day
    global step

    global ticher_one
    global discipline_one
    global time_one

    global day_discipline
    global day_time
    global day_ticher

    def name(message):
        day_ticher.append(message.text)
        msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:")
        bot.register_next_step_handler(msg, discipline)

    def time(message):
        if message.text.isdigit() == True:
            if int(message.text) >= 1 and int(message.text) <= 7:
                day_time.append(message.text)
                msg = bot.send_message(message.from_user.id, "Введите номер аудитории")
                bot.register_next_step_handler(msg, name)
            else:
                msg = bot.send_message(message.from_user.id,
                                       "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                bot.register_next_step_handler(msg, time)
        else:
            msg = bot.send_message(message.from_user.id, "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
            bot.register_next_step_handler(msg, time)

    def discipline(message):
        global day
        global step

        global ticher_two
        global discipline_two
        global time_two

        global day_discipline
        global day_time
        global day_ticher

        if message.text == "Следующий день":

            day = day + 1

            if day == 7 and step == 2:
                msg = "Заполнение первой недели."
                choice(message, msg)
                pio_1(message)
            elif day == 14:
                weeks(message)

            else:

                discipline_two.append(day_discipline)
                time_two.append(day_time)
                ticher_two.append(day_ticher)

                day_discipline = []
                day_time = []
                day_ticher = []

                msg = bot.send_message(message.from_user.id, "Ввведите название первого предмета:")
                bot.register_next_step_handler(msg, discipline)


        elif message.text == "Выходной":
            day = day + 1
            if day == 7 and step == 2:
                msg = "Заполнение первой недели."
                choice(message, msg)
                pio_1(message)
            elif day == 14:
                weeks(message)
            else:
                day_discipline.append("Пар нет, кайфуем")
                day_time.append("0")
                day_ticher.append("NAN")
                discipline_two.append(day_discipline)
                time_two.append(day_time)
                ticher_two.append(day_ticher)
                day_discipline = []
                day_time = []
                day_ticher = []
                msg = bot.send_message(message.from_user.id, "Ввведите название первого предмета:")
                bot.register_next_step_handler(msg, discipline)
        else:
            day_discipline.append(message.text)
            msg = bot.send_message(message.from_user.id, "Введите время:")
            bot.register_next_step_handler(msg, time)

    msg = bot.send_message(message.from_user.id, "Введите название предмета:")
    bot.register_next_step_handler(msg, discipline)


def choice(message, msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weekend = types.KeyboardButton('Выходной')
    nexxt = types.KeyboardButton('Следующий день')
    markup.row(weekend, nexxt)
    bot.send_message(message.from_user.id, msg)
    bot.send_message(message.from_user.id, "Первая дисциплина.", reply_markup=markup)


def weeks(message):
    global step
    global day

    if message.text == 'I неделя':

        step = 1
        msg = "Заполнение первой недели."
        choice(message, msg)
        pio_1(message)

    elif message.text == 'II неделя':

        step = 2
        msg = "Заполнение второй недели."
        choice(message, msg)
        pio_2(message)

    if day == 14:
        day = 0

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        weekend = types.KeyboardButton('I')
        nexxt = types.KeyboardButton('II')
        markup.row(weekend, nexxt)
        msg = bot.send_message(message.from_user.id, "Какая сейчас идёт неделя ?", reply_markup=markup)
        bot.register_next_step_handler(msg, replace)


def replace(message):
    global week_now
    global data_enter
    if message.text == "I":
        week_now = 1
    elif message.text == "II":
        week_now = 2

    data_enter.append(int(date.today().day))
    data_enter.append(int(date.today().month))

    shedule_write()
    bot.send_message(message.from_user.id, "Рассписание успешно заполненно!")
    beginning(message)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    beginning(message)


@bot.message_handler(commands=['0713'])
def admin(message):
    keyboard = types.InlineKeyboardMarkup()
    enter = types.InlineKeyboardButton(text='Ввод расписания', callback_data="1")
    keyboard.add(enter)
    editing = types.InlineKeyboardButton(text='Редактирование расписания', callback_data="2")
    keyboard.add(editing)
    conversion = types.InlineKeyboardButton(text='Перевод недели', callback_data="3")
    keyboard.add(conversion)
    bot.send_message(message.from_user.id, text='Какие будут указания хозяин ?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        yes = types.KeyboardButton('Да')
        no = types.KeyboardButton('Нет')
        markup.row(yes, no)
        bot.send_message(call.from_user.id, "Хотите удалить старое расписание ?", reply_markup=markup)

        @bot.message_handler(content_types=["text"])
        def text(message):

            global ticher_one
            global discipline_one
            global time_one
            global ticher_two
            global discipline_two
            global time_two

            if message.text == 'Да':

                time_one = []
                time_two = []
                ticher_one = []
                ticher_two = []
                discipline_one = []
                discipline_two = []

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                one = types.KeyboardButton('I неделя')
                two = types.KeyboardButton('II неделя')
                markup.row(one, two)
                bot.send_message(message.from_user.id, "Хорошо", reply_markup=markup)
                msg = bot.send_message(message.from_user.id, "Рассписание на какую неделю будем заполнять ?")
                bot.register_next_step_handler(msg, weeks)
            elif message.text == 'Нет':
                beginning(message)

    if call.data == "2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton('I неделя')
        two = types.KeyboardButton('II неделя')
        today = types.KeyboardButton('На сегодня')
        tomorrow = types.KeyboardButton('На завтра')
        markup.row(one, two)
        markup.row(today, tomorrow)
        bot.send_message(call.from_user.id, "Рассписание на какой день изменить?", reply_markup=markup)

        @bot.message_handler(content_types=["text"])
        def text(message):
            if message.text == "На сегодня" and week_now == 1:

                day_discipline = []
                day_time = []
                day_ticher = []

                def name(message):

                    day_ticher.append(message.text)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    one = types.KeyboardButton('Добавить предмет')
                    two = types.KeyboardButton('Сохранить изменения')
                    markup.row(one, two)

                    def choice_2(message):
                        if message.text == "Добавить предмет":
                            msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:",
                                                   reply_markup=types.ReplyKeyboardRemove())
                            bot.register_next_step_handler(msg, discipline)

                        elif message.text == "Сохранить изменения":
                            bot.send_message(message.from_user.id, "Изменения сохранены!")
                            ticher_one[day_week] = day_ticher
                            time_one[day_week] = day_time
                            discipline_one[day_week] = day_discipline

                            shedule_write()

                            beginning(message)

                    msg = bot.send_message(message.from_user.id, "Хотите добавить предмет или сохранить изменения?",
                                           reply_markup=markup)
                    bot.register_next_step_handler(msg, choice_2)

                def time(message):
                    if message.text.isdigit() == True:
                        if int(message.text) >= 1 and int(message.text) <= 7:
                            day_time.append(message.text)
                            msg = bot.send_message(message.from_user.id, "Введите номер аудитории:")
                            bot.register_next_step_handler(msg, name)
                        else:
                            msg = bot.send_message(message.from_user.id,
                                                   "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                            bot.register_next_step_handler(msg, time)
                    else:
                        msg = bot.send_message(message.from_user.id,
                                               "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                        bot.register_next_step_handler(msg, time)

                def discipline(message):
                    day_discipline.append(message.text)
                    msg = bot.send_message(message.from_user.id, "Введите время:")
                    bot.register_next_step_handler(msg, time)

                msg = bot.send_message(message.from_user.id, "Введите название первого предмета:",
                                       reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, discipline)

            elif message.text == "На сегодня" and week_now == 2:

                day_discipline = []
                day_time = []
                day_ticher = []

                def name(message):

                    day_ticher.append(message.text)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    one = types.KeyboardButton('Добавить предмет')
                    two = types.KeyboardButton('Сохранить изменения')
                    markup.row(one, two)

                    def choice_2(message):
                        if message.text == "Добавить предмет":
                            msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:",
                                                   reply_markup=types.ReplyKeyboardRemove())
                            bot.register_next_step_handler(msg, discipline)

                        elif message.text == "Сохранить изменения":
                            bot.send_message(message.from_user.id, "Изменения сохранены!")
                            ticher_two[day_week] = day_ticher
                            time_two[day_week] = day_time
                            discipline_two[day_week] = day_discipline
                            shedule_write()
                            beginning(message)

                    msg = bot.send_message(message.from_user.id, "Хотите добавить предмет или сохранить изменения?",
                                           reply_markup=markup)
                    bot.register_next_step_handler(msg, choice_2)

                def time(message):
                    if message.text.isdigit() == True:
                        if int(message.text) >= 1 and int(message.text) <= 7:
                            day_time.append(message.text)
                            msg = bot.send_message(message.from_user.id, "Ввеите номер аудитории:")
                            bot.register_next_step_handler(msg, name)
                        else:
                            msg = bot.send_message(message.from_user.id,
                                                   "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                            bot.register_next_step_handler(msg, time)
                    else:
                        msg = bot.send_message(message.from_user.id,
                                               "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                        bot.register_next_step_handler(msg, time)

                def discipline(message):
                    day_discipline.append(message.text)
                    msg = bot.send_message(message.from_user.id, "Введите время:")
                    bot.register_next_step_handler(msg, time)

                msg = bot.send_message(message.from_user.id, "Введите название первого предмета:",
                                       reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, discipline)

            elif message.text == "На завтра" and week_now == 1:

                day_discipline = []
                day_time = []
                day_ticher = []

                def name(message):

                    day_ticher.append(message.text)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    one = types.KeyboardButton('Добавить предмет')
                    two = types.KeyboardButton('Сохранить изменения')
                    markup.row(one, two)

                    def choice_2(message):
                        if message.text == "Добавить предмет":
                            msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:",
                                                   reply_markup=types.ReplyKeyboardRemove())
                            bot.register_next_step_handler(msg, discipline)

                        elif message.text == "Сохранить изменения":
                            bot.send_message(message.from_user.id, "Изменения сохранены!")
                            ticher_one[day_week] = day_ticher
                            time_one[day_week] = day_time
                            discipline_one[day_week] = day_discipline
                            shedule_write()
                            beginning(message)

                    msg = bot.send_message(message.from_user.id, "Хотите добавить предмет или сохранить изменения?",
                                           reply_markup=markup)
                    bot.register_next_step_handler(msg, choice_2)

                def time(message):
                    if message.text.isdigit() == True:
                        if int(message.text) >= 1 and int(message.text) <= 7:
                            day_time.append(message.text)
                            msg = bot.send_message(message.from_user.id, "Введите номер аудитории:")
                            bot.register_next_step_handler(msg, name)
                        else:
                            msg = bot.send_message(message.from_user.id,
                                                   "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                            bot.register_next_step_handler(msg, time)
                    else:
                        msg = bot.send_message(message.from_user.id,
                                               "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                        bot.register_next_step_handler(msg, time)

                def discipline(message):
                    day_discipline.append(message.text)
                    msg = bot.send_message(message.from_user.id, "Введите время:")
                    bot.register_next_step_handler(msg, time)

                msg = bot.send_message(message.from_user.id, "Введите название первого предмета:",
                                       reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, discipline)

            elif message.text == "На завтра" and week_now == 2:

                day_discipline = []
                day_time = []
                day_ticher = []

                def name(message):

                    day_ticher.append(message.text)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    one = types.KeyboardButton('Добавить предмет')
                    two = types.KeyboardButton('Сохранить изменения')
                    markup.row(one, two)

                    def choice_2(message):
                        if message.text == "Добавить предмет":
                            msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:",
                                                   reply_markup=types.ReplyKeyboardRemove())
                            bot.register_next_step_handler(msg, discipline)

                        elif message.text == "Сохранить изменения":
                            bot.send_message(message.from_user.id, "Изменения сохранены!")
                            ticher_two[day_week] = day_ticher
                            time_two[day_week] = day_time
                            discipline_two[day_week] = day_discipline
                            shedule_write()

                            beginning(message)

                    msg = bot.send_message(message.from_user.id, "Хотите добавить предмет или сохранить изменения?",
                                           reply_markup=markup)
                    bot.register_next_step_handler(msg, choice_2)

                def time(message):
                    if message.text.isdigit() == True:
                        if int(message.text) >= 1 and int(message.text) <= 7:
                            day_time.append(message.text)
                            msg = bot.send_message(message.from_user.id, "Введите номер аудитории:")
                            bot.register_next_step_handler(msg, name)
                        else:
                            msg = bot.send_message(message.from_user.id,
                                                   "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                            bot.register_next_step_handler(msg, time)
                    else:
                        msg = bot.send_message(message.from_user.id,
                                               "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                        bot.register_next_step_handler(msg, time)

                def discipline(message):
                    day_discipline.append(message.text)
                    msg = bot.send_message(message.from_user.id, "Введите время:")
                    bot.register_next_step_handler(msg, time)

                msg = bot.send_message(message.from_user.id, "Введите название первого предмета:",
                                       reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, discipline)

            if message.text == "I неделя":

                def processing_message(message):
                    k = 1
                    send_day = 0

                    while k < 8:
                        if message.text == weekdays[k]:
                            send_day = k
                            processing_day(send_day)

                        if message.text.isdigit() == True:
                            if int(message.text) == k:
                                send_day = k
                                processing_day(send_day)
                        k = k + 1

                    if send_day == 0:
                        msg = bot.send_message(message.from_user.id,
                                               "День недели введен не корректно, повторите попытку:")
                        bot.register_next_step_handler(msg, processing_message)

                msg = bot.send_message(message.from_user.id, "Введите название дня недели или порядковый номер:",
                                       reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, processing_message)

                def processing_day(send_day):

                    day_discipline = []
                    day_time = []
                    day_ticher = []

                    global day_week

                    day_week = send_day

                    def name(message):

                        day_ticher.append(message.text)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        one = types.KeyboardButton('Добавить предмет')
                        two = types.KeyboardButton('Сохранить изменения')
                        markup.row(one, two)

                        def choice_2(message):

                            global ticher_one
                            global discipline_one
                            global time_one
                            global day_week

                            if message.text == "Добавить предмет":
                                msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:",
                                                       reply_markup=types.ReplyKeyboardRemove())
                                bot.register_next_step_handler(msg, discipline)

                            elif message.text == "Сохранить изменения":
                                bot.send_message(message.from_user.id, "Изменения сохранены!")
                                ticher_one[day_week] = day_ticher
                                time_one[day_week] = day_time
                                discipline_one[day_week] = day_discipline
                                shedule_write()
                                beginning(message)

                        msg = bot.send_message(message.from_user.id, "Хотите добавить предмет или сохранить изменения?",
                                               reply_markup=markup)
                        bot.register_next_step_handler(msg, choice_2)

                    def time(message):
                        if message.text.isdigit() == True:
                            if int(message.text) >= 1 and int(message.text) <= 7:
                                day_time.append(message.text)
                                msg = bot.send_message(message.from_user.id, "Введите номер аудитории:")
                                bot.register_next_step_handler(msg, name)
                            else:
                                msg = bot.send_message(message.from_user.id,
                                                       "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                                bot.register_next_step_handler(msg, time)
                        else:
                            msg = bot.send_message(message.from_user.id,
                                                   "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                            bot.register_next_step_handler(msg, time)

                    def discipline(message):
                        day_discipline.append(message.text)
                        msg = bot.send_message(message.from_user.id, "Введите время:")
                        bot.register_next_step_handler(msg, time)

                    msg = bot.send_message(message.from_user.id, "Введите название первого предмета:",
                                           reply_markup=types.ReplyKeyboardRemove())
                    bot.register_next_step_handler(msg, discipline)

            elif message.text == "II неделя":

                def processing_message(message):
                    k = 1
                    send_day = 0

                    while k < 8:
                        if message.text == weekdays[k]:
                            send_day = k
                            processing_day(send_day)

                        if message.text.isdigit() == True:
                            if int(message.text) == k:
                                send_day = k
                                processing_day(send_day)

                        k = k + 1

                    if send_day == 0:
                        msg = bot.send_message(message.from_user.id,
                                               "День недели введен не корректно, повторите попытку:")
                        bot.register_next_step_handler(msg, processing_message)

                msg = bot.send_message(message.from_user.id, "Введите название дня недели или порядковый номер:",
                                       reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, processing_message)

                def processing_day(send_day):

                    day_discipline = []
                    day_time = []
                    day_ticher = []

                    global day_week

                    day_week = send_day

                    def name(message):

                        day_ticher.append(message.text)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        one = types.KeyboardButton('Добавить предмет')
                        two = types.KeyboardButton('Сохранить изменения')
                        markup.row(one, two)

                        def choice_2(message):

                            global ticher_two
                            global discipline_two
                            global time_two
                            global day_week

                            if message.text == "Добавить предмет":
                                msg = bot.send_message(message.from_user.id, "Ввведите название следующего предмета:",
                                                       reply_markup=types.ReplyKeyboardRemove())
                                bot.register_next_step_handler(msg, discipline)

                            elif message.text == "Сохранить изменения":
                                bot.send_message(message.from_user.id, "Изменения сохранены!")
                                ticher_two[day_week] = day_ticher
                                time_two[day_week] = day_time
                                discipline_two[day_week] = day_discipline
                                shedule_write()
                                beginning(message)

                        msg = bot.send_message(message.from_user.id, "Хотите добавить предмет или сохранить изменения?",
                                               reply_markup=markup)
                        bot.register_next_step_handler(msg, choice_2)

                    def time(message):
                        if message.text.isdigit() == True:
                            if int(message.text) >= 1 and int(message.text) <= 7:
                                day_time.append(message.text)
                                msg = bot.send_message(message.from_user.id, "Введите номер аудитории:")
                                bot.register_next_step_handler(msg, name)
                            else:
                                msg = bot.send_message(message.from_user.id,
                                                       "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                                bot.register_next_step_handler(msg, time)
                        else:
                            msg = bot.send_message(message.from_user.id,
                                                   "Введены некорректные данные! \nВведите номер пары от 1 до 7:")
                            bot.register_next_step_handler(msg, time)

                    def discipline(message):
                        day_discipline.append(message.text)
                        msg = bot.send_message(message.from_user.id, "Введите время:")
                        bot.register_next_step_handler(msg, time)

                    msg = bot.send_message(message.from_user.id, "Введите название первого предмета:",
                                           reply_markup=types.ReplyKeyboardRemove())
                    bot.register_next_step_handler(msg, discipline)

    if call.data == "3":
        global week_now
        global data_enter
        if week_now == 1:
            week_now = 2
        else:
            week_now = 1

        data_enter.append(int(date.today().day))
        data_enter.append(int(date.today().month))

        msg = bot.send_message(call.from_user.id, "Порядок недель успешно изменён.")

        @bot.message_handler(content_types=["text"])
        def text(message):
            shedule_write()
            beginning(message)


bot.polling()