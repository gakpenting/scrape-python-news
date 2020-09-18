
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getBody
def link224():
    getList(datea=None,
    content="#mainContent > div > div.compField:nth-of-type(1)",
    imajina="#mainContent > div > div:nth-child(2) > div > img",
    pagis=1,
    getDatea=None,
    replaceRegex=None,
    numero="224",
    LA_name="Cambridgeshire",
    LA_pr="https://www.cambridgeshire.gov.uk/news",
    links=r"https://www.cambridgeshire.gov.uk/api/delivery/projects/cambridgeshire/entries/search?fields=publishedDate%2Cthumbnail%2Cexcerpt%2CentryTitle%2Csys.uri&linkDepth=1&orderBy=%5B%7B%22desc%22%3A%22publishedDate%22%7D%5D&pageIndex=0&pageSize=12&where=%5B%7B%22field%22%3A%22sys.contentTypeId%22%2C%22in%22%3A%5B%22newsArticle%22%5D%7D%2C%7B%22field%22%3A%22sys.uri%22%2C%22exists%22%3Atrue%7D%2C%7B%22field%22%3A%22sys.versionStatus%22%2C%22equalTo%22%3A%22published%22%7D%5D",
    listas=None,
    datesss=None,
    replaceDate=None,
    title=None,
    getBody=getBody,
    imajinasi=None,
    linkedin="https://www.cambridgeshire.gov.uk",
    href="a",
    linkedin2="https://www.cambridgeshire.gov.uk")
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="224",LA_name="Cambridgeshire",LA_pr="https://www.cambridgeshire.gov.uk/news",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        
        link=links
        headers={'accessToken':'96kYysfMhmRIzxq90aH1Xm1SdgmXPYQUnW9b9frCg6HhUxnF','User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        r = requests.get(link, timeout=15,verify=False,headers=headers)
            
            # print(soup)
        lista=r.json()["items"]
            # print(lista[0].prettify())
            
        
        
        for a in lista:
                
            s=a["publishedDate"] if a["publishedDate"] else "1 January 2020"
            
                # print(s)
                # print(a.select_one("a").get("href"))
            imajin=""
            titulos=a["entryTitle"] if a["entryTitle"] else ""
                
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=titulos
                        )
                coki=getBody(linkedin+a["sys"]["uri"],content=content,imajin=imajina)
                papa.body=coki[0] if len(coki) > 0 and coki else ""
                papa.image=linkedin2+coki[1] if len(coki) > 0 and coki[1] != "" else imajin
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


