import telebot




def main():
    bot = telebot.TeleBot('1288987415:AAFkTpWoqYqXJ9yMpuqWSXqsjrGaW1fm24k');
    @bot.message_handler(commands=['start'])
    def start_bot(message):
        bot.send_message(message.chat.id, 'Привет')

    print("[INFO] Bot is started")
    bot.infinity_polling()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
