
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getBody,getDate as getDatea
def link230():
    getList(
        datea=None,
        content=".content-page-holder > p:not(:nth-of-type(1))",
        imajina="sam",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="230",
        LA_name="South Lakeland",
        LA_pr="https://www.southlakeland.gov.uk/news/",
        links="https://www.southlakeland.gov.uk/news/",
        listas=".news-list > li",
        datesss=None,
        replaceDate=None,
        title="a",
        getBody=getBody,
        imajinasi="sam",
        linkedin="https://www.southlakeland.gov.uk",
        href="a",
    linkedin2="",
    dayfirst=True)
def getList(dayfirst=False,datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="230",LA_name="South Lakeland",LA_pr="https://www.southlakeland.gov.uk/news/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        
        namber=str(number)
        setop=False
        link=links
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
            
        
        for a in lista:
                
            s=a.getText()
            cop=re.search("[\d\/]", s)
            s=cop.group() if cop else "1 january 2020"
            
                # print(s)
                # print(a.select_one("a").get("href"))
            imajin=linkedin2+a.select_one(imajinasi).get("src") if a.select_one(imajinasi) else "" if imajinasi else ""
            titulos=a.select_one("a").get("title") if a.select_one("a") else ""
                
            if compareDate(s,lastDate,dayfirst):
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s,dayfirst),                        
                        title=a.select_one(title).getText().replace('\n', ' ').replace('\r', '').strip() if a.select_one(title) else titulos if titulos else ""
                        )
                coki=getBody(linkedin+a.select_one(href).get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina)
                papa.body=coki[0] if len(coki) > 0 and coki else ""
                papa.image=linkedin2+coki[1] if len(coki) > 0 and coki[1] != "" else imajin
                papa.save()
                    
            
                   
    except Exception as e:
        print("err "+numero+" ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates,dayfirst):
    dt = parse(dates.strip(),dayfirst=dayfirst)
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate,dayfirst):
    dt = parse(dates.strip(),dayfirst=dayfirst)
    dateCompare = date(2020, 6, 1)  
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared


