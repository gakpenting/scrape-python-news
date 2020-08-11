import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
def link51():
    getList(
    numero="51",
    LA_name="Torridge",
    LA_pr="https://www.torridge.gov.uk/article/12994/News",
    links="https://www.torridge.gov.uk/article/13019/RSS-News-Feed",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
def getBody(link,**kwargs):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        r = requests.get(link.strip(), timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select_one("div#bodytext").getText().replace('\n', ' ').replace('\r', '').strip() if soup.select_one("div#bodytext") else ""
        image=soup.select_one("div#bodytext img").get("src") if soup.select_one("div#bodytext img") else ""
        panda1=a      
        
        return [panda1,image]
     
    except:
        return None