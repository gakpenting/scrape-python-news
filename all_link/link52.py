import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
import re
def link52():
    getList(
    numero="52",
    LA_name="West Devon",
    LA_pr="https://www.westdevon.gov.uk/article/569/News-",
    links="https://www.westdevon.gov.uk/article/569/News-?p=",
    listas="div.grid__cell",
    datesss=None,
    replaceDate=None,
    replaceRegex=None,
    getDatea=getDate,
    title="a",
    getBody=getBody,
    imajinasi="img",
    linkedin="",
    href="a",
    linkedin2="")
def getDate(link):
    try:
        s=None
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select(".maincontent__left > div > *:not(p):not(a):not(img):not(div)")
        for i in a:
            cop=re.search(r"\d{1,2}\s\w+\s\d{4,}", i.getText().strip())
            if cop:            
                s=cop.group()
        return s if s else "1 January 2020"
     
    except Exception as e:
        print(str(e))
        return "1 January 2020"
def getBody(link):
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one(".a-body").getText()
        
        
        
        return [panda1,image]
     
    except:
        return None