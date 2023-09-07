import aiogram
import config
import requests
import logging
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
from aiogram.types import ChatActions
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import requests
from bs4 import BeautifulSoup
# IMport Database
import database


logging.basicConfig(level=logging.INFO)

# from bot import category as bot_categoriy_list
index_of_day = 0

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
bot_categoriy_list = [
    'Понедельник ☘️',
    'Вторник 🍀',
    'Среда 🌿',
    'Четверг 🎍',
    'Пятница 🍁',
    'Суббота 🎋',
]

def random_image():
    img_url = "https://random.imagecdn.app/500/500"
    img = requests.get(img_url).content
    with open('img.png' , 'wb') as handler :
        handler.write(img)

def get_info ():
    url = 'https://portal.esstu.ru/bakalavriat/45.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml' )

    arr = []
    for text in soup.find_all('tr'):
        temp_arr = []
        for rez in text.find_all('td'):
            rez = rez.get_text()
            rez = rez.encode("latin-1").decode('cp1251')
            temp_arr.append(rez)
        arr.append(temp_arr)
    return arr


markup3 = ReplyKeyboardMarkup()
markup3.add(KeyboardButton('Назад 🔙'))
for i in bot_categoriy_list:
    markup3.add(KeyboardButton(i))

all_category = KeyboardButton('Nedelya 2️⃣')
random_quotes = KeyboardButton('Nedeiya 1️⃣')
hello = ReplyKeyboardMarkup().add(
    random_quotes).add(all_category)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if database.chesk_user_into_database( user_id=message.chat.id , chat_id=message.chat.id ):
        # print(message)
        database.adding_user_to_data_base(user_id=message.chat.id , chat_id=message.chat.id , user_name=message.chat.first_name , user_surname=message.chat.last_name)
        await bot.send_sticker(message.chat.id , sticker='CAACAgIAAxkBAAEKOgJk9v01ThGdXzaBYWKK0eE_kFmAhgACNhYAAlxA2EvbRm7S3ZV6DTAE')
        await message.reply("Привет! " + message.chat.first_name + " !\nДобро пожаловать в бот группу B743")
        await bot.send_message(message.chat.id , 'выберите неделю 🗓️' , reply_markup=hello)
    else :
        await bot.send_sticker(message.chat.id , sticker='CAACAgIAAxkBAAEKOgJk9v01ThGdXzaBYWKK0eE_kFmAhgACNhYAAlxA2EvbRm7S3ZV6DTAE')
        await message.reply("Привет! " + message.chat.first_name + " !\nMi pomnim tebya , rad videt tebya в бот группу B743")
        await bot.send_message(message.chat.id , 'выберите неделю 🗓️' , reply_markup=hello)
    print(message)
    
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(message.chat.id , '❗️Внимание❗️ \nЭтот бот назодится в стадии разработки и тестирование.🛠️\nПри возникновение ощибки или бага , пожалуста отправте скриншот @behruzbegmatov 😉.\nСпасибо за исползование нашего бота❤️')

@dp.message_handler(commands=['menu'])
async def help_command(message: types.Message):
    await message.reply('выберите неделю 🗓️' , reply_markup=hello)
@dp.message_handler()
async def echo(message: types.Message):
    global index_of_day
    if message.text == 'Nedeiya 1️⃣':
        await bot.send_message(message.chat.id , 'Хорошо \nВыберите день 😎' , reply_markup=markup3)
        index_of_day = 1
    elif message.text == 'Nedelya 2️⃣':
        await bot.send_message(message.chat.id , 'Хорошо \nВыберите день 🤩' , reply_markup=markup3)
        index_of_day = 2
    elif message.text == 'Назад 🔙' :
        await bot.send_message(message.chat.id , 'выберите неделю 🗓️' , reply_markup=hello)
        index_of_day = 0
    for kun in bot_categoriy_list :
        
        if kun == message.text :
            rapisani = get_info()
            chars_to_remove = ["[", "]" , "'" ]
            if index_of_day == 1:
                if message.text == 'Понедельник ☘️' :
                    ansver = rapisani[2]
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Вторник 🍀':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[3]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Среда 🌿':
                    ansver = rapisani[4]
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Четверг 🎍':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[5]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Пятница 🍁':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[6]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Суббота 🎋':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[7]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
            if index_of_day == 2:
                if message.text == 'Понедельник ☘️' :
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[8]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Вторник 🍀':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[9]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Среда 🌿':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[10]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Четверг 🎍':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[11]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Пятница 🍁':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[12]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )
                elif message.text == 'Суббота 🎋':
                    time = str(rapisani[1])
                    time = time.replace('n' , ' ')
                    time = time.replace('\ ' , '')
                    ansver = rapisani[13]
                    ansver = str(ansver).replace('n' , ' ')
                    ansver = str(ansver).replace('\ ' , '')
                    ansver = str(ansver).replace(',' , '\n')
                    for carts in chars_to_remove :
                        ansver = ansver.replace(carts , '')
                        time = time.replace(carts , '')
                    await bot.send_message(message.chat.id , time )
                    await bot.send_message(message.chat.id , ansver )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)