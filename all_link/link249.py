
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getDate as getDatea
def link249():
    getList(
        datea=None,
        content="article > p:not(:last-child)",
        imajina="sam",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="249",
        LA_name="Southwark",
        LA_pr="https://www.southwark.gov.uk/news",
        links="https://www.southwark.gov.uk/news",
        listas="a.noPadding",
        datesss="time",
        replaceDate=None,
        title=getTitle,
        getBody=getBody,
        imajinasi=".category-card-image",
        linkedin="https://www.southwark.gov.uk",
        href="a",
        linkedin2="https://www.southwark.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="249",LA_name="Southwark",LA_pr="https://www.southwark.gov.uk/news",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        
        namber=str(number)
        setop=False
        link=links
        headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "method":"GET",
        "cookie":'visid_incap_1892657=+pQKLAHJQ4armDHqgSgQJKsUTl8AAAAAQUIPAAAAAADl2luhzs/ndQlZx9HqPZ46; CookieNotice=["statistics=1","marketing=1"]; _ga=GA1.3.2146456171.1598952660; _fbp=fb.2.1598952661351.1115192120; incap_ses_1121_1892657=CaTRCfsZ4A42iy/PrZeOD76VXV8AAAAASIHkIGujRATidgnXNUY+QQ==; _gid=GA1.3.208684330.1599968708'}
        r = requests.get(link, timeout=15,verify=True,headers=headers)
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
                
            s=None
            if datesss:
                s=a.select_one(datesss).getText().replace(replaceDate,"") if replaceDate else a.select_one(datesss).getText()
            if replaceRegex:
                cop=re.search(replaceRegex, a.select_one(datesss).getText())
                s=cop.group() if cop else ""
            if getDatea:
                s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
            
                # print(a.select_one("a").get("href"))
            imajin=linkedin2+re.sub("background-image:url\(|\)","",a.select_one(imajinasi).get("style"))
            
                
            if compareDate(s,lastDate):
                
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=title(linkedin+a.get("href"),title="article > h1")
                        )
                coki=getBody(linkedin+a.get("href"),content=content,imajin=imajina)
                papa.body=coki[0] if len(coki) > 0 and coki else ""
                papa.image=linkedin2+coki[1] if len(coki) > 0 and coki[1] != "" else imajin
                papa.save()
                
                    
                
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
def getBody(link,content="sam",imajin="sam",linkedin2=""):
    panda1=""
    image=""
    try:
        headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "method":"GET",
        "cookie":'visid_incap_1892657=+pQKLAHJQ4armDHqgSgQJKsUTl8AAAAAQUIPAAAAAADl2luhzs/ndQlZx9HqPZ46; CookieNotice=["statistics=1","marketing=1"]; _ga=GA1.3.2146456171.1598952660; _gid=GA1.3.1619770431.1598952660; _fbp=fb.2.1598952661351.1115192120; incap_ses_1115_1892657=eMjLD92OlUf0ylWXwUZ5DyTzTl8AAAAAAbQn2zBB6Z/4va8LPPOUwQ=='}
        
        r = requests.get(link.strip(), timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        
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
def getTitle(link,title="sam"):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        
        panda1=soup.select(title) if soup.select(title) else ""
        
        return panda1
     
    except Exception as e:
        print(str(e))
        return panda1

