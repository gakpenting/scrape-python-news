import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
import re
def link58():
    getList(
        pagis=1,
    numero="58",
    LA_name="Eastbourne",
    LA_pr="lewes-eastbourne.gov.uk/news-room/",
    links="https://www.lewes-eastbourne.gov.uk/lewes-district-council-news/?lister103784p=",
    listas="li.oBoxItem",
    datesss="span.item-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="a",
    getBody=getBody,
    imajinasi="sam",
    linkedin="https://www.lewes-eastbourne.gov.uk",
    href="a",
    linkedin2="")
def getDate(link):
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
def getBody(link):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one("div#-ux-content > div:nth-of-type(3)").getText().replace('\n', ' ').replace('\r', '').strip() if soup.select_one("div#-ux-content > div:nth-of-type(3)") else ""
        image="https://www.lewes-eastbourne.gov.uk"+soup.select_one("div.asset > img").get("src") if soup.select_one("div.asset > img") else ""
        return [panda1,image]
     
    except:
        return None