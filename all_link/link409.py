
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re

from all_link.helpers.helper import getDate as getDatea
def link409():
    getList(
        datea=None,
        getDatea=None,
numero="409",
LA_name="Richmondshire",
LA_pr="richmondshire.gov.uk/news/",
    links="https://www.richmondshire.gov.uk/news/latest-news/",
    listas="body > main > div.container > ul > li",
    datesss="p",
    replaceDate=None,
    replaceRegex="\d{1,2}\/\d{1,2}\/\d{4}",
    dayfirst=True,
    title="h2",
    getBody=getBody,
    content=".container.content-holder",
    imajina="sam",
    linkedin="https://www.richmondshire.gov.uk",
    href="a",
    linkedin2="")

def getList(datea=None,replaceRegex=None,replaceRegexTitle=None,content="sam",imajina="",getDatea=None,dayfirst=False,numero=None,LA_name=None,LA_pr=None,links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi="None",linkedin="",href="a",linkedin2=""):
    
    
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        link=links
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        r = requests.get(link, timeout=30,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        lista=soup.select(listas)
        # print(len(lista))
        
            
        
        # if len(lista) == 0:
        
        for a in lista:
            
            s=None
            if datesss:
                s=a.select_one(datesss).getText().replace(replaceDate,"") if replaceDate else a.select_one(datesss).getText()
            # print(s)
            
            if replaceRegex:
                cop=re.search(replaceRegex, a.select_one(datesss).getText())
                s=cop.group() if cop else "1 January 2020"
            if getDatea:
                s=getDatea(linkedin+a.select_one(href).get("href"),date=datea,replaceRegex=replaceRegex,replaceDate=replaceDate)
            # print(a)
            # print(a.select_one("a").get("href"))
            
            imajin=linkedin2+a.select_one(imajinasi).get("src") if a.select_one(imajinasi) else "" if imajinasi else ""
            if compareDate(s,lastDate,dayfirst):
                carabrim=""
                carabrim=a.select_one(title).getText().replace('\n', ' ').replace('\r', '').strip()
                if replaceRegexTitle:
                    carabrim=re.sub(replaceRegexTitle, "", carabrim)
                papa,created=Links.get_or_create(
                    LA_name=LA_name,
                    LA_pr=LA_pr,
                    date=getDate(s,dayfirst),                        
                    title=carabrim
                    )
                coki=getBody(link=linkedin+a.select_one(href).get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina,linkedin2=linkedin2)
                papa.body=coki[0] if len(coki) > 0 and coki else ""
                papa.image=coki[1] if len(coki) > 0 and coki[1] != "" else imajin
                papa.save()
                    
            
        
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
    dt = parse(dates.strip(),dayfirst=dayfirst)
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
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=30,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        
        panda=soup.select(content) if soup.select(content) else []
        
        # print(soup)
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        image=soup.select(imajin) if soup.select(imajin) else []
        # print(soup)
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
