import requests
from bs4 import BeautifulSoup

def get_text():
    url = "https://www.playground.ru/news"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, "html.parser")
    #test=get_tags(soup)
    href=get_href(soup)
    conteiner=soup.find("div", {"class":"post-title"})
    text=conteiner.find('a')
    text=str(text.text)
    text=text+'\n'+"[Источник]"+"("+href+")"
    #test = test+text
    return(text)
def get_href(soup):
    conteiner=soup.find("div", {"class":"post-title"})
    href=conteiner.find('a').get('href')
    return(href)
def get_tags(soup):
    conteiner=soup.find("div", {"class":"post-metadata"})
    tags=conteiner.find("a")
    tags=str(tags.text)
    test = "#"+tags+"\n"
    return (test)
def get_pic():
    url = "https://www.playground.ru/news"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, "html.parser")
    conteiner=soup.find("article", {"class":"post"})
    img=conteiner.find("img").get('src')
    return(img)