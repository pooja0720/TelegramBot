from Adafruit_IO import Client
import os
aio = Client os.getenv('Username','ActiveKey')
from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  aio.send('Light',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned ON')
def demo2(bot,update):
    aio.send('Light',0)
    chat_id = bot.message.chat_id
    bot.message.reply_text('Light turned OFF')

def demo3(bot,update):
    aio.send('Fan',1)
    chat_id = bot.message.chat_id
    bot.message.reply_text('Fan turned ON')

def demo4(bot,update):
    aio.send('Fan',0)
    chat_id = bot.message.chat_id
    bot.message.reply_text('Fan turned OFF')

def main (bot,update):
    a= bot.message.text
    if a =="Turn on light":
      demo1(bot,update)
    elif a =="Turn off light":
      demo2(bot,update)
    elif a =="Turn on fan":
      demo3(bot,update)
    elif a =="Turn off fan":
      demo4(bot,update)

bot_token = os.getenv('bot_token')
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text, main))
u.start_polling()
u.idle()
