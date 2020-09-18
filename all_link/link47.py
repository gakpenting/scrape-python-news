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
    datesss="div.post-detail",
    replaceDate=None,
    replaceRegex=r"\d{1,2}\s\w+\s\d{4,}",
    title="h3",
    getBody=getBody,
    imajinasi="img",
    linkedin="",
    href="a",
    linkedin2="")
def getBody(link,**kwargs):
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select("div#content > *:not(h2):not(h1):not(.single-date):not(#comments):not(.clear)")
        s=""
        for j in a:
            s+=j.getText().replace('\n', ' ').replace('\r', '').strip()
        panda1=s
        
        
        return [panda1,image]
     
    except:
        return None