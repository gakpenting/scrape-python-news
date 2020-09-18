import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
import re
def link53():
    getList(
    numero="53",
    LA_name="Bournemouth, Christchurch and Poole",
    LA_pr="https://www.bcpcouncil.gov.uk/News/News-Articles/news-articles.aspx",
    links="https://www.bcpcouncil.gov.uk/News/News-Articles/news-articles.aspx?Listing_List_GoToPage=",
    listas="div.sys_subitem",
    datesss="dd.sys_news-datepublished",
    replaceDate=None,
    replaceRegex=r"\d{1,}\/\d{1,}\/\d{4,}",
    getDatea=None,
    title="a",
    getBody=getBody,
    imajinasi="sam",
    linkedin="https://www.bcpcouncil.gov.uk",
    href="a",
    linkedin2="")

def getBody(link,**kwargs):
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select(".sys_news-record > p")
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()     
        
        return [panda1,image]
     
    except:
        return None