import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
def link44():
    getList(
    numero="44",
    LA_name="East Devon",
    LA_pr="https://eastdevon.gov.uk/news",
    links="https://eastdevon.gov.uk/news/newsrss/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="https://eastdevon.gov.uk/",
    href="link",
    linkedin2="")
def getBody(link):
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select_one("section[role='main']").getText().replace('\n', ' ').replace('\r', '').strip() if soup.select_one("section[role='main']") else ""
        image="https://eastdevon.gov.uk"+soup.select_one("figure img").get("src") if soup.select_one("figure img") else ""
        panda1=a      
        
        return [panda1,image]
     
    except:
        return None