
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.helpers.helper import getDate as getDatea,getBody
import re
import json
def link198():
    getList(
        datea=None,
        content="article > div > div > div > div",
        imajina="figure > a > img",
        pagis=0,
        getDatea=None,
        replaceRegex=None,
       numero="198",
    LA_name="Argyll and Bute",
    LA_pr="https://www.argyll-bute.gov.uk/news",
        links=None,
        listas="tbody > tr",
        datesss=".date-display-single",
        replaceDate=None,
        title=".views-field-title",
        getBody=getBody,
        imajinasi="sam",
        linkedin="https://www.argyll-bute.gov.uk",
        href="a",
        linkedin2="",
    dayfirst=True
    )


def getList(dayfirst=False,datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="258",LA_name="Eastleigh",LA_pr="https://www.eastleigh.gov.uk/your-weekly-borough-news",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link="https://www.argyll-bute.gov.uk/views/ajax"
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            data={"view_name":"latest_news","view_display_id":"page_1","page":number}
            r = requests.post(link,data=data, timeout=15,verify=False,headers=headers)
            soup=None
            a=json.loads(r.text)    
            if not a[1]:
                break  
            soup = BeautifulSoup(a[1]["data"], 'html.parser')
            
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
                    s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
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
        
    

def getDate(dates,dayfirst=False):
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






