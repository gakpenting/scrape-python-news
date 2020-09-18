
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getDate as getDatea,getBody
import ast
def link264():
    getList(
        datea="time",
        content=".container > article[role='main'] *:not(h1):not(h4)",
        imajina="sam",
        pagis=0,
        getDatea=getDatea,
        replaceRegex=None,
        numero="264",
        LA_name="Hertfordshire",
        LA_pr="https://www.hertfordshire.gov.uk/about-the-council/news/media-centre.aspx",
        links="https://www.hertfordshire.gov.uk/about-the-council/news/news-archive/news-archive.aspx?pageIndex=",
        listas=".resultsList__content",
        datesss=None,
        replaceDate=None,
        title=".resultsList__itemMainTitle",
        getBody=getBody,
        imajinasi="img",
        linkedin="https://www.hertfordshire.gov.uk/about-the-council/news/news-archive/",
        href="a",
        linkedin2="https://www.hertfordshire.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="264",LA_name="Hertfordshire",LA_pr="https://www.hertfordshire.gov.uk/about-the-council/news/media-centre.aspx",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            isoDate="2020-06-01T00:00:00"
            if len(lastDate) > 0:
                isoDate=lastDate[0].date.isoformat()    
            link='https://cms-hcc.cloud.contensis.com/api/delivery/projects/website/entries/search?linkDepth=1&orderBy=[{"desc":"dateTimeOfPublication"}]&pageIndex=%s&pageSize=6&where=[{"field":"sys.versionStatus","equalTo":"published"},{"or":[{"and":[{"field":"includeInSearch","exists":true},{"field":"includeInSearch","equalTo":true}]},{"field":"includeInSearch","exists":false}]},{"field":"sys.contentTypeId","equalTo":"news"},{"field":"dateTimeOfPublication","greaterThanOrEqualTo":"%s"}]' % (namber,isoDate)
            headers={'accessToken':'ZnlyviS9DcLiTnTUoJCLTgryTr1buC1KtAwYSX32f64A0RM5','User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            r = requests.get(link, timeout=15,verify=False,headers=headers)
            # print(link)
            
            
            lista=r.json()["items"]
            # print(lista[0].prettify())
            
            # print(len(lista))
            folklore=0
            if len(lista) == 0:
                break
            for a in lista:
                folklore+=1
                
                s=a["dateTimeOfPublication"]
                
                
                # print(a.select_one("a").get("href"))
                pok=a["listingImage"]["asset"]["sys"]["uri"] if a["listingImage"] else ""
                imajin=linkedin2+pok
                
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a["title"]
                        )
                    coki=""
                    for j in a["articleBody"]:
                        if j["type"]=="markup" and j["value"].strip() != "":
                            coki+=BeautifulSoup(j["value"],"html.parser").text
                    papa.body=coki
                    papa.image=imajin
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


