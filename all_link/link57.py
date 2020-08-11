import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
import re
def link57():
    getList(
        pagis=0,
    numero="57",
    LA_name="Brighton and Hove",
    LA_pr="https://new.brighton-hove.gov.uk/news",
    links="https://new.brighton-hove.gov.uk/news/callback?&page=",
    listas="article",
    datesss="ul.top-story--meta",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h3",
    getBody=getBody,
    imajinasi="img",
    linkedin="https://new.brighton-hove.gov.uk",
    href="a",
    linkedin2="https://new.brighton-hove.gov.uk")
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
        panda=soup.select("article > *:not(div):not(section)")
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        return [panda1,image]
     
    except:
        return None