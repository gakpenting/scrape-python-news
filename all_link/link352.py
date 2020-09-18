
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
import html
from all_link.helpers.helper import getDate as getDatea,getBody
from dateutil.relativedelta import relativedelta
import ast
def link352():
    getList(
        datea=None,
        content=".bodyText > p",
        imajina="sam",
        pagis=0,
        getDatea=None,
        replaceRegex=None,
        numero="352",
        LA_name="Carmarthenshire",
        LA_pr="http://newsroom.carmarthenshire.gov.wales/",
        links=None,
        listas=".latest-new-item-row",
        datesss=".pull-left",
        replaceDate=None,
        title="h3",
        getBody=getBody,
        imajinasi="sam",
        linkedin="http://newsroom.carmarthenshire.gov.wales",
        href="a",
        linkedin2=""
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="352",LA_name="Carmarthenshire",LA_pr="http://newsroom.carmarthenshire.gov.wales/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link="http://newsroom.carmarthenshire.gov.wales/Umbraco/Api/ApiDataLoader/GetNextNewsArticles?numberToSkip=%s&lang=en-GB&pageId=23614" % (namber)
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            r = requests.get(link, timeout=15,verify=False,headers=headers)
            soup=None
            if r.headers['content-type']=="application/json":
                a=json.loads(r.text)
                soup = BeautifulSoup(a["html"], 'html.parser')
            else:
                soup = BeautifulSoup(ast.literal_eval(r.text), 'html.parser')
            
            
            
            # print(soup.prettify())
            
            lista=soup.select(listas)
            
            if len(lista) == 0:
                break
            for a in lista:
                
                s=get_past_date(a.select_one(datesss).getText())
                
                # if datesss:
                #     s=a.select_one(datesss).getText().replace(replaceDate,"") if replaceDate else a.select_one(datesss).getText()
                # if replaceRegex:
                #     cop=re.search(replaceRegex, a.select_one(datesss).getText())
                #     s=cop.group() if cop else ""
                # if getDatea:
                #     s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
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
            number+=5
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
def get_past_date(str_days_ago):
    TODAY = datetime.now()
    
    splitted = str_days_ago.strip().split()
    if len(splitted) == 1 and splitted[0].lower() == 'today':
        return str(TODAY.isoformat())
    elif len(splitted) == 1 and splitted[0].lower() == 'yesterday':
        date = TODAY - relativedelta(days=1)
        return str(date.isoformat())
    elif splitted[1].lower() in ['hour', 'hours', 'hr', 'hrs', 'h']:
        date = datetime.now() - relativedelta(hours=int(splitted[0]))
        return str(date.date().isoformat())
    elif splitted[1].lower() in ['day', 'days', 'd']:
        date = TODAY - relativedelta(days=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['wk', 'wks', 'week', 'weeks', 'w']:
        date = TODAY - relativedelta(weeks=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['mon', 'mons', 'month', 'months', 'm']:
        date = TODAY - relativedelta(months=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['yrs', 'yr', 'years', 'year', 'y']:
        date = TODAY - relativedelta(years=int(splitted[0]))
        return str(date.isoformat())
    else:
        return "1 January 2020"

