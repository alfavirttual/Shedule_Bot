import telebot
from config import token


class Bot:
    __token = None

    def __init__(self, token=token):
        self.__token = token
        self.bot = telebot.TeleBot(token)

    def return_bot(self):
        return self.bot
