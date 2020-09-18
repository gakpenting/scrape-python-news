
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getBody,getDate as getDatea
def link229():
    getList(
        datea=None,
        content=".text_companyprofile",
        imajina="",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="229",
        LA_name="City of London",
        LA_pr="https://news.cityoflondon.gov.uk/",
        links="https://news.cityoflondon.gov.uk/?h=1&t=News,news",
        listas=None,
        datesss=None,
        replaceDate=None,
        title=None,
        getBody=getBody,
        imajinasi=None,
        linkedin="",
        href="a",
        linkedin2=""
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="229",LA_name="City of London",LA_pr="https://news.cityoflondon.gov.uk/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        
        
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
        lista=soup.select_one("#ppmodule_allheadlines > div > div > script")
            # print(lista[0].prettify())
            
        # \[[\W\w]+\]    
        p = re.compile(r'\[[\W\d]+\]')
        cop=p.findall(str(lista))
        text = eval(cop[0])
        # print(text[0])
        
        for a in text:
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            luink="https://news.cityoflondon.gov.uk/services/getheadlines.php?archive=1&type=1&releases=[%%22%s%%22]&preview=&umbrella=0" % (a)
            r = requests.get(luink, timeout=15,verify=False,headers=headers)
            s=json.loads(r.text)["1"]["date"]
                           
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=json.loads(r.text)["1"]["title"]
                        )
                coki=getBody(json.loads(r.text)["1"]["shareurl"],content=content,imajin=imajina)
                papa.body=coki[0] if len(coki) > 0 and coki else ""
                imajin=re.sub("background-image:url\(|\);","",json.loads(r.text)["1"]["featuredimage"])
                papa.image="https:"+imajin if imajin != "" else ""
                papa.save()
                    
            else:
                break
                    # break
            
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


