
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getBody,getDate as getDatea
def link247():
    getList(
        datea=".article__date",
        content=".content-header__summary, .markup",
        imajina="sam",
        pagis=0,
        getDatea=getDatea,
        replaceRegex=None,
        numero="247",
        LA_name="Lewisham",
        LA_pr="https://lewisham.gov.uk/news",
        links="https://lewisham.gov.uk/newsandupdates?offset=",
        listas=".article",
        datesss=None,
        replaceDate=None,
        title=".article__title",
        getBody=getBody,
        imajinasi="sam",
        linkedin="https://lewisham.gov.uk",
        href=".article__link",
        linkedin2=""
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="247",LA_name="Lewisham",LA_pr="https://lewisham.gov.uk/news",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number*10)
            setop=False
            link="https://lewisham.gov.uk/api/search?offset=%s&page=f6ec6d76-b7ec-42d0-81d3-13010e0f11d8" % (namber)
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            r = requests.get(link, timeout=15,verify=False,headers=headers)
            soup=None
            b=json.loads(r.text)
            soup = BeautifulSoup(b["items"], 'html.parser')
            
            
            # print(soup)
            lista=soup.select(listas)
            
            
            if len(lista) == 0:
                break
            for a in lista:
                
                s=None
                if datesss:
                    s=a.select_one(datesss).getText().replace(replaceDate,"") if replaceDate else a.select_one(datesss).getText()
                if replaceRegex:
                    cop=re.search(replaceRegex, a.select_one(datesss).getText())
                    s=cop.group() if cop else ""
                if getDatea:
                    s=getDatea(linkedin+a.select_one(href).get("href"),date=datea,replaceDate="Published on: ")
                # print(s)
                # print(a.select_one("a").get("href"))
                imajin=linkedin2+a.select_one(imajinasi).get("src") if a.select_one(imajinasi) else "" if imajinasi else ""
                titulos=a.select_one("a").get("title") if a.select_one("a") else ""
                
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a.select_one(title).getText().replace('\n', ' ').replace('\r', '').strip() if a.select_one(title) else titulos if titulos else ""
                        )
                    coki=getBody(linkedin+a.select_one(href).get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina)
                    papa.body=coki[0] if len(coki) > 0 and coki else ""
                    papa.image=linkedin2+coki[1] if len(coki) > 0 and coki[1] != "" else imajin
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


