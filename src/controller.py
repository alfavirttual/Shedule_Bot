from datetime import date, datetime

class Controller:
    "Класс - обрботчик запросов пользователя"

    __num_week = 1
    __day_week = date.today().isoweekday()
    __time = datetime.now().time()
    def __init__(self, message):
        self.message = message

    def start(self, message):
        if message == "start":
            #вывод меню с помощью view







