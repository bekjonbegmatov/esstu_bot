# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor

# import requests
# from bs4 import BeautifulSoup

from config import TOKEN

# # bot = Bot(token=TOKEN)
# # dp = Dispatcher(bot)
# def get_info ():
#     url = 'https://portal.esstu.ru/bakalavriat/45.htm'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml' )

#     arr = []
#     for text in soup.find_all('tr'):
#         temp_arr = []
#         for rez in text.find_all('td'):
#             rez = rez.get_text()
#             rez = rez.encode("latin-1").decode('cp1251')
#             temp_arr.append(rez)
#         arr.append(temp_arr)
#     # result = str(arr)
#     return arr

# # @dp.message_handler(commands=['start'])
# # async def process_start_command(message: types.Message):
# #     await message.reply("Привет!\nДобро пожаловать в бот группу B743")

# # @dp.message_handler(commands=['help'])
# # async def process_help_command(message: types.Message):
# #     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

# # @dp.message_handler(commands=['dars'])
# # async def process_help_command(message: types.Message):
# #     await message.reply(get_info())
    



# # @dp.message_handler()
# # async def echo_message(msg: types.Message):
# #     await bot.send_message(msg.from_user.id, msg.text)

# # if __name__ == '__main__':
# #     executor.start_polling(dp)
# #!/usr/bin/python

# # This is a simple echo bot using the decorator mechanism.
# # It echoes any incoming text messages.

# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
API_TOKEN = TOKEN

# bot = telebot.TeleBot(API_TOKEN)
# nedelya = 0
# def gen_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("1️⃣", callback_data="cb_yes"),
#         InlineKeyboardButton("2️⃣", callback_data="cb_no"))
#     return markup

# def callback_query(call):
#     if call.data == "cb_yes":
#         nedelya = 0
#         print(nedelya)
#     elif call.data == "cb_no":
#         nedelya = 1
#         print(nedelya)


# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, "Привет!\nДобро пожаловать в бот группу B743", reply_markup=gen_markup())
#     # bot.reply_to(message, "Привет!\nДобро пожаловать в бот группу B743")

# @bot.message_handler(commands=['dars'])
# def send_welcome(message):
#     chars_to_remove = ["[", "]" , "'" , "n"]
    
#     for sps in get_info():
#         mystr = str(sps)
#         for char in chars_to_remove:
#             mystr = mystr.replace(char, "")
#         mystr = mystr.replace(',' , '\n')
#         mystr = mystr.replace('_' , '-----нет пары-----')
#         bot.send_message(message.chat.id, mystr )


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


# bot.infinity_polling()
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)
nedelya = 0
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("1️⃣", callback_data="cb_yes"),
                               InlineKeyboardButton("2️⃣", callback_data="cb_no"))
    return markup
def den_mocup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    list_data = [ 'Пнд' , 'Втр' , 'Срд' , 'Чтв' , 'Птн' , 'Сбт']
    for dat in list_data :
        markup.add(InlineKeyboardButton(dat , callback_data=dat))
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "недели один")
        nedelya = 1
        bot.send_message(call.id, "выберите день", reply_markup=den_mocup())
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "недели два")
        nedelya = 2
        bot.send_message(call.id, "выберите день", reply_markup=den_mocup())


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    # 
    bot.send_message(message.chat.id, "Привет!\nДобро пожаловать в бот группу B743")
    bot.send_message(message.chat.id, "выбритой неделю", reply_markup=gen_markup())

bot.infinity_polling()