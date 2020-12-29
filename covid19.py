import requests
from bs4 import BeautifulSoup

def get_stat():
    url = "https://xn----7sbahrplyfdaxfotk.xn--p1ai/orlovskaya-oblast/"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, "html.parser")
    text=get_text(soup)
    conteiner=soup.find("div", {"class":"listing-item"})
    title1=conteiner.find('h4')
    title1=str(title1.text)
    title2=conteiner.find('p')
    title2=str(title2.text)
    title="*"+title1+"*"+"\n"+title2
    title=title+"\n"+text+'\n'+"[Источник]"+"(https://coronavirus-control.ru/koronavirus-v-orlovskoj-oblasti-na-28-dekabrya-2020-goda-skolko-zabolevshix-na-segodnya/)"
    #title = title+"\n"+text
    #print(title)
    return(title)
def get_text(soup):
    #conteiner=soup.find("div", {"class":"layout-four section"})
    #text=conteiner.findAll("div")
    #print(text)
    article_text = ''
    article = soup.find("div", {"class":"total_area row pt-3 pb-3"}).findAll('div')
    for element in article:
        article_text += '\n' + ' - '.join(element.findAll(text = True))
    #print(article_text)
    #text=str(text.text)
    #text = text
    print(article_text)
    numb=get_num()
    text="\n"+"*"+numb+" - за сутки"+"*"+article_text
    return (text)
def get_num():
    url = "https://koronainfo.ru/orlovskaya-oblast"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, "html.parser")
    num=soup.find("div", {"class":"today"})
    numb=num.find('span', {"class":"bold"})
    numb=str(numb.text)
    print(numb)
    return(numb)