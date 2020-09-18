import requests
from datetime import datetime,date,timedelta 
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import re
from all_link.helpers.helper import getDate,getBody
def link222():
    getList(
    numero="222",
    LA_name="West Berkshire",
    LA_pr="https://info.westberks.gov.uk/news",
    links="https://info.westberks.gov.uk/news",
    listas="#newsnewsitems > * > *",
    datesss="span.timedate",
    replaceDate=None,
    title="a",
    getBody=getBody,
    content="#defaultcontent > *:not(h1)",
    imajina=".rimage > img",
    linkedin="https://info.westberks.gov.uk",
    href="a",
    linkedin2="")


def getList(datea=None,replaceRegex=None,replaceRegexTitle=None,content="sam",imajina="",getDatea=None,dayfirst=False,numero=None,LA_name=None,LA_pr=None,links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi="None",linkedin="",href="a",linkedin2=""):
    
    
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        link=links
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        lista=soup.select(listas)
        # print(len(lista))
            
        
        # if len(lista) == 0:
        
        for a in lista:
            s=None
            if datesss:
                s=a.select_one(datesss).getText().replace(replaceDate,"")+"20" if replaceDate else a.select_one(datesss).getText()+"20"
            s=re.sub(r"^\d{2}:\d{2}pm\s-|^\d{2}:\d{2}am\s-", "", s)
            
            if getDatea:
                s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
            # print(s)
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


