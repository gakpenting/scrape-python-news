
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getBody
import re
def link202():
    getList(
    pagis=1,
    numero="202",
    LA_name="Renfrewshire",
    LA_pr="http://www.renfrewshire.gov.uk/news",
    links="http://www.renfrewshire.gov.uk/news?p=",
    listas=".summarytile",
    datesss="h2",
    replaceDate=None,
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    getDatea=getDate,
    datea="div.textblock > p:nth-last-child(2),div.textblock > p:nth-last-child(1)",
    title="h2",
    getBody=getBody,
    content="div.intro, div.textblock",
    imajina=".left img",
    imajinasi="sam",
    linkedin="http://www.renfrewshire.gov.uk",
    href="a",
    linkedin2="http://www.renfrewshire.gov.uk")
def getDate(link=None,date="sam",replaceDate=None,replaceRegex=None):
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1="1 January 2020"
        cobi=""
        for num in soup.select(date):
            cobi+=num.getText()+" "
        # print(cobi)
        panda1=cobi if soup.select(date) else "1 January 2020"
        # print(panda1)
        if replaceRegex:
            cop=re.search(replaceRegex, panda1)
            panda1=cop.group() if cop else "1 January 2020"
            # print(panda1)
        
        
        return panda1
     
    except:
        
        return "1 January 2020"

