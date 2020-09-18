
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re

from all_link.helpers.helper import getDate as getDatea
def link373():
    getList(
    numero="373",
        LA_name="Bradford",
        LA_pr="https://www.bradford.gov.uk/browse-all-news/press-releases/current-news-releases/",
    links="https://www.bradford.gov.uk/news-rss-feed",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".bodyText",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
def getList(xmlType="lxml-xml",datea=None,getDatea=None,content="sam",imajina="",numero=None,LA_name=None,LA_pr=None,links=None,listas=None,datesss="pubDate",replaceDate="",titles="title",getBody=None,imajinasi=None,linkedin="",href="link",linkedin2=""):
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        link=links
        # print(link)
        headers={"Cookie":"incap_ses_1120_1845735=glL3JCsBWy3OTiB9MQqLDxMYWF8AAAAA9dpyEuaNoRCzrkjG+u2i+g==; visid_incap_1845735=3LxByr7RQxqFsxfx0f/cUBMYWF8AAAAAQUIPAAAAAACR3BFevtUNfl08wY4GonWW","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
        r = requests.get(link.strip(),verify=True, timeout=15,headers=headers)
        soup = BeautifulSoup(r.text, xmlType)
        # print(soup)
        
        lista=soup.select(listas)
        # print(lista[0].select_one("link").getText())
        for a in lista:
            s=None
            if datesss:
                s=a.select_one(datesss).getText()
            if getDatea:
                s=getDatea(linkedin+a.select_one(href).getText().replace('\n', ' ').replace('\r', '').strip(),datea)
            # print(compareDate(s.getText(),lastDate))
            # print(a.select_one("title").getText())
            tambo=a.select_one(href).getText().replace('\n', ' ').replace('\r', '').strip() if a.select_one(href).getText().strip() != "" else a.select_one(href).get("href")
            
            image=getBody(linkedin+tambo,content=content,imajin=imajina,linkedin2=linkedin2)
            title=a.select_one(titles).getText().replace('\n', ' ').replace('\r', '').strip()
            imajin=linkedin2+a.select_one(imajinasi).getText() if a.select_one(imajinasi) else "" if imajinasi else ""
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                    LA_name=LA_name,
                    LA_pr=LA_pr,
                    date=getDate(s),
                    title=title                    
                    )
                papa.body=image[0] if len(image) > 0 else ""
                papa.image=image[1] if len(image) > 0 and image[1] != "" else imajin
                papa.save()
                
            
                
    except Exception as e:
        print("err link "+numero+" ", str(e) )
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

def getBody(link,content="sam",imajin="sam",linkedin2=""):
    panda1=""
    image=""
    try:
        headers={"Cookie":"incap_ses_1120_1845735=6R06HKFcJQm8gyB9MQqLD+MZWF8AAAAAzU3vYX9yOvjrx31Rd8oD/Q==; visid_incap_1845735=3LxByr7RQxqFsxfx0f/cUBMYWF8AAAAAQUIPAAAAAACR3BFevtUNfl08wY4GonWW","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=15,verify=True,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup)
        
        panda=soup.select(content) if soup.select(content) else []
        # print(panda)
        
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        image=soup.select(imajin) if soup.select(imajin) else []
        tabi=""
        if len(image)> 1:
            for a in image:
                tabi+=linkedin2+a.get("src")+"|"
            image=tabi
        else:
            image=linkedin2+soup.select_one(imajin).get("src") if soup.select_one(imajin) else ""
        return [panda1,image]
     
    except Exception as e:
        print(str(e))
        return [panda1,image]