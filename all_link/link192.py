
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.helpers.helper import getDate as getDatea,getBody
import re
def link192():
    getList(
    pagis=1,
    numero="192",
    LA_name="Fermanagh and Omagh",
    LA_pr="https://www.fermanaghomagh.com/news/",
    links="https://www.fermanaghomagh.com/news/page/",
    listas=".listing-cards__item",
    datesss=".date-published",
    replaceDate=None,
    replaceRegex="\d{1,2}(st|nd|th|rd)\s\w+\s\d{4}",
    getDatea=None,
    title=".show-for-sr",
    getBody=getBody,
    content=".block__content",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")

def getList(dayfirst=False,datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero=None,LA_name=None,LA_pr=None,links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link=links+namber
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            r = requests.get(link, timeout=15,verify=False,headers=headers)
            soup=None
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # print(soup)
            lista=soup.select(listas)
            # print(lista[0].prettify())
            
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
                    s=getDatea(linkedin+a.select_one(href).get("href"),date=datea,replaceDate=replaceDate,replaceRegex=replaceRegex)
                
                
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
                    coki=getBody(linkedin+a.select_one(href).get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina,linkedin2=linkedin2)
                    papa.body=coki[0] if len(coki) > 0 and coki else ""
                    pattern = re.compile("background-image: url\(|\)")
                    newstring = pattern.sub("", a.select_one("div").get("style")) if a.select_one("div").get("style") else ""
                    papa.image=newstring if newstring != "" else ""
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
        
    

def getDate(dates, dayfirst=False):
    dt=None
    if type(dates) == date:
        dt=dates
    else:
        dt = parse(dates.strip(),dayfirst=dayfirst)
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate,dayfirst=False):
    try:
        dt = parse(dates.strip(),dayfirst=dayfirst)
        dateCompare = date(2020, 6, 1)  
        if len(lastDate)>0:
            dateLen=lastDate[0].date
            dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
        date2 = date(dt.year, dt.month, dt.day)
        dateCompared = date2 > dateCompare          
        return dateCompared
    except Exception as e:
        # print("err ",e)
        return False


