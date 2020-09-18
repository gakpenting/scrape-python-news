
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.helpers.helper import getDate as getDatea,getBody
import re
def link144():
    getList(
    pagis=1,
    numero="144",
    LA_name="Stroud",
    LA_pr="https://www.stroud.gov.uk/news-archive",
    links="https://www.stroud.gov.uk/news-archive?page=",
    listas="h3 > a,h2 > a:not(.see_all)",
    datesss=None,
    replaceDate=None,
    replaceRegex=None,
    getDatea=getDatea,
    datea="#page_body > div.container > div > div > div.col-md-8 > p:nth-child(3)",
    title="h2",
    getBody=getBody,
    content="#page_body > div.container > div > div > div.col-md-8 > p:not(:nth-child(3))",
    imajina="#sidebar > img",
    imajinasi="sam",
    linkedin="https://www.stroud.gov.uk",
    href="a",
    linkedin2="https://www.stroud.gov.uk")

import json
import re
def getList(dayfirst=False,datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero=None,LA_name=None,LA_pr=None,links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link=links+namber
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            r = requests.get(link, timeout=15,verify=False,headers=headers)
            soup=None
            if r.headers['content-type']=="application/json":
                a=json.loads(r.text)
                soup = BeautifulSoup(a["html"], 'html.parser')
            else:
                soup = BeautifulSoup(r.text, 'html.parser')
            
            # print(soup)
            lista=soup.select(listas)
            # print(lista[0].prettify())
            
            if len(lista) == 0:
                break
            for a in lista:
                s=None
                
                    
                if getDatea:
                    s=getDatea(linkedin+a.get("href"),date=datea,replaceDate=replaceDate,replaceRegex="\w+,\s+\d{1,2}\s\w+,\s\d{4}")
                
                # print(s)
                
                # print(a.select_one("a").get("href"))
                
                
                if compareDate(s,lastDate,dayfirst):
                    
                    papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s,dayfirst),                        
                        title=a.getText().replace('\n', ' ').replace('\r', '').strip() 
                        )
                    coki=getBody(linkedin+a.get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina,linkedin2=linkedin2)
                    papa.body=coki[0] if len(coki) > 0 and coki else ""
                    papa.image=coki[1] if len(coki) > 0 and coki[1] != "" else ""
                    papa.save()
                    
                else:
                    setop=True
                    # break
            if setop:
                break
            number+=1
    except Exception as e:
        print("err "+numero+" ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates, dayfirst=False):
    dt=None
    if type(dates) == date:
        dt=dates
    else:
        dt = parse(dates.strip(),dayfirst=dayfirst)
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate,dayfirst=False):
    try:
        dt = parse(dates.strip(),dayfirst=dayfirst)
        dateCompare = date(2020, 6, 1)  
        if len(lastDate)>0:
            dateLen=lastDate[0].date
            dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
        date2 = date(dt.year, dt.month, dt.day)
        dateCompared = date2 > dateCompare          
        return dateCompared
    except Exception as e:
        # print("err ",e)
        return False


