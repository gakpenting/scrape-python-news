import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
import re
def link56():
    getList(
    numero="56",
    LA_name="East Sussex",
    LA_pr="https://news.eastsussex.gov.uk/",
    links="https://news.eastsussex.gov.uk/page/",
    listas="article",
    datesss="time.entry-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h1",
    getBody=getBody,
    imajinasi="img",
    linkedin="",
    href="a",
    linkedin2="")
def getDate(link):
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one("span.entry-meta-date.updated").getText().replace('\n', ' ').replace('\r', '').strip()     
        
        
        return panda1
     
    except:
        return "1 January 2020"
def getBody(link):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one("div.entry-content").getText().replace('\n', ' ').replace('\r', '').strip()     
        
        
        return [panda1,image]
     
    except:
        return None