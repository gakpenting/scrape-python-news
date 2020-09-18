import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
def link43():
    getList(
    numero="43",
    LA_name="Devon",
    LA_pr="https://www.devonnewscentre.info/",
    links="https://www.devonnewscentre.info/feed/",
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
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select("div#content p")
        image=soup.select_one("div.single-thumbnail.pull-right img").get("src") if soup.select_one("div.single-thumbnail.pull-right img") else ""
        s=""
        c=0
        for j in a[1:len(a)]:
            s+=j.getText().replace('\n', ' ').replace('\r', '').strip() if j else ""
        panda1=s
        
        
        return [panda1,image]
     
    except:
        return None