
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getBody,getDate as getDatea
def link244():
    getList(
        datea=None,
        content="#description",
        imajina=".content_wrapper img",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="244",
        LA_name="Enfield",
        LA_pr="https://new.enfield.gov.uk/news-and-events/",
        links="https://new.enfield.gov.uk/_odata/adx_blogpost_newsandevents?$top=6",
        listas=".newsandeventsitem",
        datesss=".card-text",
        replaceDate="Published on: ",
        title="h2",
        getBody=getBody,
        imajinasi="sam",
        linkedin="https://new.enfield.gov.uk/news-and-events/",
        href="a",
        linkedin2="https://new.enfield.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="244",LA_name="Enfield",LA_pr="https://new.enfield.gov.uk/news-and-events/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        
        namber=str(number)
        setop=False
        link=links
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        r = requests.get(link, timeout=15)
        b=json.loads(r.text)
            
            
            # print(soup)
        lista=b["value"]
            # print(lista[0].prettify())
            
        
        for a in lista:
                
            s=a["adx_date"]
            
                # print(s)
                # print(a.select_one("a").get("href"))
            
                
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a["adx_name"]
                        )
                coki=getBody(linkedin+a["adx_partialurl"],content=content,imajin=imajina)
                papa.body=coki[0] if len(coki) > 0 and coki else ""
                papa.image=linkedin2+coki[1] if len(coki) > 0 and coki[1] != "" else ""
                papa.save()
                    
                
                    # break
            
    except Exception as e:
        print("err "+numero+" ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = parse(dates.strip())
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = parse(dates.strip())
    dateCompare = date(2020, 6, 1)  
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared


