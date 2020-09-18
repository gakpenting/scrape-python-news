
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
import urllib.parse
from all_link.helpers.helper import getDate as getDatea,getBody
def link356():
    getList(
        datea=None,
        content="sam",
        imajina="",
        pagis=0,
        getDatea=None,
        replaceRegex=None,
        numero="356",
        LA_name="Isle of Anglesey",
        LA_pr="https://www.anglesey.gov.uk/en/Newsroom/Newsroom.aspx#/",
        links=None,
        listas=None,
        datesss=None,
        replaceDate=None,
        title=None,
        getBody=None,
        imajinasi=None,
        linkedin="",
        href="a",
        linkedin2="https://www.anglesey.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="356",LA_name="Isle of Anglesey",LA_pr="https://www.anglesey.gov.uk/en/Newsroom/Newsroom.aspx#/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link="""
            https://cms-ynysmon.cloud.contensis.com/api/delivery/projects/website/entries/search?linkDepth=1&orderBy=[{"desc":"publishedDate"}]&pageIndex=%s&pageSize=10&where=[{"field":"sys.versionStatus","equalTo":"published"},{"field":"sys.contentTypeId","equalTo":"news"},{"or":[]},{"field":"sys.language","equalTo":"en-GB"},{"field":"isFeatured","equalTo":true}]
            """ % (namber)
            headers={"accesstoken":"yNir4845WTD79uhNeYK49Xk43o3nxkqpDIbV4n8tli8UT0fC",'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            # pan=urllib.parse.quote(link)
            r = requests.get(link, timeout=15,verify=False,headers=headers)
            soup=None
            b=json.loads(r.text)["items"]
               
            
            # print(soup)
            lista=b
            # print(lista[0].prettify())
            
            if len(lista) == 0:
                break
            for a in lista:
                
                s=a['publishedDate']
                # print(s)
                # print(a.select_one("a").get("href"))
                
                
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a["title"]
                        )
                    cekak=""
                    for c in a["article"]:
                        if c["type"] == "articleHTML":
                            aha=BeautifulSoup(c["value"],"html.parser").text
                            cekak+=aha+" "
                    papa.body=cekak
                    papa.image=linkedin2+a["commonEntryFields"]["thumbnailImage"]["asset"]["sys"]["uri"] if a["commonEntryFields"]["thumbnailImage"]["asset"]["sys"]["uri"].strip() != "" else ""
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


