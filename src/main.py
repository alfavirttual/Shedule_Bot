from view import View
from controller import Controller
from model import PostgreSQL
from bot import Bot


def main():
    bot = Bot().return_bot()
    view = View(bot)
    model = PostgreSQL()
    controller = Controller(model, view, bot)
    controller.hendler()
    print("[INFO] Bot is started")
    bot.infinity_polling()


if __name__ == '__main__':
    main()
