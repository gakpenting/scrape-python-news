import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
import re
def link60():
    getList(
        pagis=1,
    numero="60",
    LA_name="Rother",
    LA_pr="http://www.rother.gov.uk/News",
    links="https://www.rother.gov.uk/news/page/",
    listas="article",
    datesss="p > strong",
    replaceDate="Published: ",
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")
def getDate(link,**kwargs):
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select("article > *:not(div):not(section)")
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        return panda1
     
    except:
        return "1 January 2020"
def getBody(link,**kwargs):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one("article.rother_news-article").getText().replace('\n', ' ').replace('\r', '').strip() if soup.select_one("article.rother_news-article") else ""
        image=""
        return [panda1,image]
     
    except:
        return None