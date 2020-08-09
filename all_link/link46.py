import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
def link46():
    getList(
    dayfirst=True,
    numero="46",
    LA_name="Mid Devon",
    LA_pr="https://www.middevon.gov.uk/news-items/",
    links="https://www.middevon.gov.uk/news-items/",
    listas="div.inner div.row:not([class='divider row'])",
    datesss="div.creationDate p:nth-of-type(1)",
    replaceDate="Posted on: ",
    title="div.caption h2",
    getBody=getBody,
    imajinasi="img",
    linkedin="https://www.middevon.gov.uk",
    href="a",
    linkedin2="https://www.middevon.gov.uk")
def getBody(link,**kwargs):
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select("main > div.container > *:not(div):not(ul)")
        s=""
        for j in a:
            s+=j.getText().replace('\n', ' ').replace('\r', '').strip()
        panda1=s
        
        
        return [panda1,image]
     
    except:
        return None