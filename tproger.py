import requests
from bs4 import BeautifulSoup

def get_post():
    url = "https://tproger.ru/news/"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, "html.parser")
    text=get_text(soup)
    href=get_href(soup)
    conteiner=soup.find("div", {"class":"post-title"})
    title=conteiner.find('h2')
    title=str(title.text)
    title="*"+title+"*"+"\n"+text+'\n'+"[Источник]"+"("+href+")"
    #title = title+"\n"+text
    print(title)
    return(title)
def get_href(soup):
    conteiner=soup.find("article")
    href=conteiner.find('a').get('href')
    print(href)
    return(href)
def get_text(soup):
    conteiner=soup.find("div", {"class":"entry-content"})
    text=conteiner.find("p")
    text=str(text.text)
    text = text
    return (text)