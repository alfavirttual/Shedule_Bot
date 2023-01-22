from datetime import date, datetime


class Controller:
    "Класс - обрботчик запросов пользователя"

    __num_week = 1
    __day_week = date.today().isoweekday()
    __time = datetime.now().time()

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self, message):
        self.view.send_message(message, "Hallo")
            #вывод меню с помощью view


    def handler(self, message):
        pass







