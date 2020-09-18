import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
def link48():
    getList(
    numero="48",
    LA_name="Plymouth",
    LA_pr="https://www.plymouth.gov.uk/newsroom",
    links="https://www.plymouth.gov.uk/newsroom",
    listas="table.views-table > tbody > tr",
    datesss="span.date-display-single",
    replaceDate=None,
    title="a",
    getBody=getBody,
    linkedin="https://www.plymouth.gov.uk",
    href="a",
    linkedin2="")

def getBody(link,**kwargs):
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select_one("[property='content:encoded']").getText() if soup.select_one("[property='content:encoded']") else ""
        panda1=a
        
        
        return [panda1,image]
     
    except:
        return None