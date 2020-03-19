# MIT License

# Copyright(c) 2020 Sabu Siyad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from telegram.ext import Updater, MessageHandler, run_async, Filters
from http import client
from random import randint

import config

updater = Updater(config.BOT_API, use_context=True)
dp = updater.dispatcher


def ToNum(s):
    try:
        return int(s)
    except ValueError:
        return False


def GetRes(n, date=False):
    cases = [f"/{n}", f"/{n}/math"]
    if 1500 < n < 2000:
        cases = [f"/{n}/year"]
    connection = client.HTTPConnection("numbersapi.com")
    connection.request("GET", cases[randint(0, len(cases)-1)])
    return connection.getresponse().read().decode()


def GetNum(s):
    list = [ToNum(n) for n in s.split(" ") if ToNum(n) != False]
    if list != []:
        return list[randint(0, len(list)-1)]
    else:
        return False


@run_async
def Grab(update, context):
    num = GetNum(update.effective_message.text)
    if num:
        update.message.reply_markdown(f"*Did you know❔* {GetRes(num)}❕")


dp.add_handler(MessageHandler(Filters.text, Grab))


if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
