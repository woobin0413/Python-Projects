# -*- coding: utf-8 -*-
import telegram   #텔레그램 모듈을 가져옵니다.
import os, requests
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules
from bs4 import BeautifulSoup as bs
import time, itertools
from multiprocessing import Pool # Pool import하기


<<<<<<< HEAD
my_token = ''   #토큰을 변수에 저장합니다.
=======
my_token = '#'   #토큰을 변수에 저장합니다.
>>>>>>> cdb98408951f672c4a9cd582109ddeabd3ecac92
#
# bot = telegram.Bot(token = my_token)   #bot을 선언합니다.
#
# # updates = bot.getUpdates()  #업데이트 내역을 받아옵니다.
# # # chat_id = bot.getUpdates()[-1].message.chat.id #최신 문자보낸 사람의 id를 받아온다
# # # bot.sendMessage(chat_id = chat_id, text="저는 봇입니다.")
# # for u in updates :   # 내역중 메세지를 출력합니다.
# #
# #     # print(u.message.chat.id)
#
# id_channel = bot.sendMessage(chat_id='@ben_notice', text="I'm bot").chat_id

dir_now = os.path.dirname(os.path.abspath(__file__))  # real path to dirname
print('start telegram chat bot')

# photo reply function
def get_photo(bot, update) :
    print("Photo received")
    print(update.message)
    file_path = os.path.join(dir_now, 'from_telegram.png')
    photo_id = update.message.photo[-1].file_id  # photo 번호가 높을수록 화질이 좋음
    photo_file = bot.getFile(photo_id)
    photo_file.download(file_path)
    update.message.reply_text('photo saved')

# file reply function
def get_file(bot, update) :
    print("File received")
    print(update.message)
    file_url = os.path.join(dir_now, update.message.document.file_name)
    file_id_short = update.message.document.file_id
    bot.getFile(file_id_short).download(file_url)
    update.message.reply_text('file saved')



# message reply function
def get_message(bot, update):
    update.message.reply_text("got text")
    # update.message.reply_text(update.message.text)
    req = requests.get('https://weather.com/weather/tenday/l/' + update.message.text + ':4:US')
    html = req.text
    soup = bs(html, 'html.parser')
    days = soup.findAll('span', {'class': 'date-time'})
    temps = soup.select('#twc-scrollabe > table > tbody > tr > td.temp > div')

    total = ''
    for day, temp in zip(days, temps):
        update.message.reply_text(day.text + " :" + temp.text)

# help reply function
def help_command(bot, update) :
    update.message.reply_text("/help = what can I help? \n/weather = weather condition? ")
# weather condition function
def weather_command(bot, update) :
    update.message.reply_text("Type your zipcode: ")

updater = Updater(my_token)

#Filters.text는 텍스트에 대해 응답하며 이때 get_message 함수를 호출합니다.
#get_message 호출시 got text 와 받은 메세지를 답장합니다.
message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', help_command)
updater.dispatcher.add_handler(help_handler)

weather_handler = CommandHandler('weather', weather_command)
updater.dispatcher.add_handler(weather_handler)

photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()

