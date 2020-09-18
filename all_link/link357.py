
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
def link357():
    getList(
        datea=None,
        content="sam",
        imajina="",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="357",
        LA_name="Monmouthshire",
        LA_pr="https://www.monmouthshire.gov.uk/latest-news/",
        links="https://www.monmouthshire.gov.uk/latest-news/",
        listas=None,
        datesss=None,
        replaceDate=None,
        title=None,
        getBody=None,
        imajinasi=None,
        linkedin="",
        href="a",
        linkedin2=""
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="357",LA_name="Monmouthshire",LA_pr="https://www.monmouthshire.gov.uk/latest-news/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        
        
        link=links
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup=None
        
        soup = BeautifulSoup(r.text, 'html.parser')
            
            # print(soup)
        lista=soup.select("article")
            # print(lista[0].prettify())
            
            
        for a in lista:
            s=a.select_one("time.entry-date").getText()
                
                # print(s)
                # print(a.select_one("a").get("href"))
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a.select_one("h1").getText().replace('\n', ' ').replace('\r', '').strip() 
                        )
                
                papa.body=a.select_one(".page-content").getText()
                papa.image=a.select_one("figure > img").get("src") if a.select_one("figure > img") else ""
                papa.save()
                    
                
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


