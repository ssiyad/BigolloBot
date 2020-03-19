from telegram.ext import Updater, MessageHandler, run_async, Filters
from http import client

import config

updater = Updater(config.BOT_API, use_context=True)
dp = updater.dispatcher


def GetNum(s):
    try:
        return int(s)
    except ValueError:
        return False

def GetRes(n):
    connection = client.HTTPConnection("numbersapi.com")
    connection.request("GET", f"/{n}")
    return connection.getresponse().read().decode()


@run_async
def Grab(update, context):
    num = GetNum(update.effective_message.text)
    if num:
        update.message.reply_markdown(f"*Did you know❔* {GetRes(num)}❕")


dp.add_handler(MessageHandler(Filters.text, Grab))


if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
