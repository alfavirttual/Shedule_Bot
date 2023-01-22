import telebot
from telebot import types
import numpy as np


class View():

    def __init__(self, bot):
        self.bot = bot

    def send_message(self, message, text):
        self.bot.send_message(message.chat.id, text)

    def create_button(self, message, button_name, coord, text):
        __markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(len(button_name)):
            button_name[i] = types.KeyboardButton(button_name[i])
        button_name = np.reshape(button_name, coord)

        for i in range(coord[0]):
            __markup.row(*button_name[i])
        self.bot.send_message(message.from_user.id, text, reply_markup=__markup)


