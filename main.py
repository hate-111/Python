import os
from background import keep_alive
import json
import pip

pip.main(['install', 'pytelegrambotapi'])
import telebot

name = None

from telebot import types

bot = telebot.TeleBot('7186120436:AAHOD7eRSAGETuCsDpSHmw0qR12_5pMN8vM')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
     bot.reply_to(message, 'Какой красивый хамстер!')


@bot.message_handler(commands=['start'])
def start(message):
     file = open('./hamzter.jpg', 'rb')
     bot.send_photo(message.chat.id, file)
     markup = types.InlineKeyboardMarkup()
     btn1 = types.InlineKeyboardButton('ЛС создателя',
                                       url='https://t.me/tt_hate')
     markup.row(btn1)
     btn2 = types.InlineKeyboardButton(
         'перети по реф силке создателя',
         url='https://t.me/hamster_kOmbat_bot/start?startapp=kentId7111292601')
     btn3 = types.InlineKeyboardButton('канал хамстера',
                                       url='https://t.me/hamster_kombat')
     markup.row(btn2, btn3)
     bot.reply_to(message, 'Какой красивый хамстер!', reply_markup=markup)


@bot.message_handler(commands=['hamster'])
def start(message):
     file = open('./homyak.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['help'])
def start(message):
     file = open('./homyak.jpg', 'rb')
     bot.send_photo(message.chat.id, file)
     bot.send_message(
         message.chat.id,
         'Все команды данного шедевра   :   /hamster   - единственный адекватный хомяк ,   /hamster1    -    первый хамстер,   /hamster2     -       первый хамстер,       /hamster3     -       второй хамстер,     /hamster4      -      третий хамстер ,     /hamster5      -        четвёртый хамстер,   /hamster6         -           пятый хамстер,    /hamster7          -          шестой хамстер,   /hamster8        -      седьмой хамстер, /sticker                  -                    стикеры с хамстер комбатом ( пока что только один'
     )


@bot.message_handler(commands=['hamster1'])
def start(message):
     file = open('./hamstern1.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster2'])
def start(message):
     file = open('./hamstern2.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster3'])
def start(message):
     file = open('./hamstern3.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster3'])
def start(message):
     file = open('./hamstern3.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster4'])
def start(message):
     file = open('./hamstern4.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster5'])
def start(message):
     file = open('./hamstern5.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster6'])
def start(message):
     file = open('./hamstern6.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster7'])
def start(message):
     file = open('./hamstern7.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['hamster8'])
def start(message):
     file = open('./hamstern8.jpg', 'rb')
     bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['sticker'])
def start(message):
     file = open('./sticker.webp', 'rb')
     bot.send_sticker(message.chat.id, file)


bot.polling(none_stop=True)
