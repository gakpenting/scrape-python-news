
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate
def link406():
    getList(
    numero="406",
    LA_name="North Ayrshire",
    LA_pr="north-ayrshire.gov.uk/news",
    links="https://www.north-ayrshire.gov.uk/news/news-archive.aspx?SyndicationType=1",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#main-content > div.content-container > div.sys_none.sys_themed.sys_theme-none > div > p",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

def getBody(link,content="sam",imajin="sam",linkedin2=""):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=30,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        
        panda=soup.select(content) if soup.select(content) else []
        
        # print(soup)
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        image=soup.select(imajin) if soup.select(imajin) else []
        # print(soup)
        tabi=""
        if len(image)> 1:
            for a in image:
                tabi+=linkedin2+a.get("src")+"|"
            image=tabi
        else:
            image=linkedin2+soup.select_one(imajin).get("src") if soup.select_one(imajin) else ""
        return [panda1,image]
     
    except Exception as e:
        print(str(e))
        return [panda1,image]
