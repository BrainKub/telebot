import telebot
import requests
from bs4 import BeautifulSoup

def get_freebie(bot, message):
    url = "https://vgtimes.ru/tags/%D1%85%D0%B0%D0%BB%D1%8F%D0%B2%D0%B0/"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, "html.parser")
    #test=get_tags(soup)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.findAll('a', '{favoritesnew}')
    for i in range(len(texts[:-16]), -1, -1):
        txt = str(i + 1) + ') Источник' + texts[i].text
        bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')