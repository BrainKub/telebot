import telebot
import requests
import os
from bs4 import BeautifulSoup
import playground
import tproger
import covid19

HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
	}

bot = telebot.TeleBot('1416836323:AAE6msCm5oT6ty09aHZfQwrQnWBSytqIDnY');
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Новости','Статистика COVID19')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, чем я могу тебе помочь?', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Новости":
        text=playground.get_text()
        photo=playground.get_pic()
        text2=tproger.get_post()
        bot.send_photo(message.chat.id, photo, caption=text, parse_mode="Markdown")
        bot.send_message(message.chat.id, text2, parse_mode="Markdown")
        #bot.send_message(message.chat.id, text, parse_mode="Markdown", disable_web_page_preview=False)
    elif message.text == "Статистика COVID19":
        text=covid19.get_stat()
        #bot.send_message(message.chat.id, "В разработке 0_0")
        #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIByV_o6Z71P1Z1qrjtMtNkMz4YYDtmAAK5IgAC6VUFGKhTf2tl6fwtHgQ')
        bot.send_message(message.chat.id, text, parse_mode="Markdown", disable_web_page_preview=True)
    else:
        msg = message.text
        bot.send_message(message.from_user.id, "Я тебя не понимаю 0_о")
        print(msg)
@bot.message_handler(content_types=['sticker'])
def stickers_id(message):
    sticker_id = message.sticker.file_id
    bot.send_sticker(message.chat.id, sticker_id)
    bot.send_message(message.chat.id, 'ID стикера: '+'```'+sticker_id+'```', parse_mode="Markdown")
bot.polling(none_stop=True, interval=0)
