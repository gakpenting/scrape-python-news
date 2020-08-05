import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
def link47():
    getList(
    numero="47",
    LA_name="North Devon",
    LA_pr="https://www.devon.gov.uk/northdevonnews/",
    links="https://www.devon.gov.uk/northdevonnews/page/",
    listas="div.row.post",
    datesss="time.published.updated",
    replaceDate=None,
    title="span.headline.h4",
    getBody=getBody,
    imajinasi="img",
    linkedin="https://www.southderbyshire.gov.uk",
    href="a",
    linkedin2="https://www.southderbyshire.gov.uk")
def getBody(link):
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select("article p")
        s=""
        for j in a:
            s+=j.getText().replace('\n', ' ').replace('\r', '').strip()
        panda1=s
        
        
        return [panda1,image]
     
    except:
        return None