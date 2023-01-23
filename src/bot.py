import telebot
from config import token


class Bot:

    def __init__(self, token=token):
        self.__token = token
        self.bot = telebot.TeleBot(token)

    def starting_bot(self):
        print("[INFO] Bot is started")
        self.bot.infinity_polling()

    def return_bot(self):
        return self.bot
