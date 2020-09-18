import csv
ta=None
with open('papa.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ta=list(csv_reader)
# print(ta[0])
# csvList=[]
# numba=0
def golek(numba,name,pr):
    popo="""
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link%s():
    getList(
    numero="%s",
    LA_name="%s",
    LA_pr="%s",
    links="https://www.cheltenham.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > *:not(h2):not(.date):not(ul):not(img)",
    imajina="#content > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

""" % (str(numba),str(numba),name,pr)
    return popo
def golek1(numba,name,pr):
    popo1="""
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link%s():
    getList(
    pagis=1,
    numero="%s",
    LA_name="%s",
    LA_pr="%s",
    links="https://www.thurrock.gov.uk/news?page=",
    listas="div.views-row",
    datesss=".date-display-single",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content="div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div > *",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.thurrock.gov.uk",
    href="a",
    linkedin2="https://www.thurrock.gov.uk")


""" % (str(numba),str(numba),name,pr)
    return popo1
def golek2(numba,name,pr):
    popo2="""
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
def link%s():
    getList()
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="%s",LA_name="%s",LA_pr="%s",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
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
            if r.headers['content-type']=="application/json":
                a=json.loads(r.text)
                soup = BeautifulSoup(a["html"], 'html.parser')
            else:
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
                    s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
                # print(s)
                # print(a.select_one("a").get("href"))
                imajin=linkedin2+a.select_one(imajinasi).get("src") if a.select_one(imajinasi) else "" if imajinasi else ""
                titulos=a.select_one("a").get("title") if a.select_one("a") else ""
                
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a.select_one(title).getText().replace('\\n', ' ').replace('\\r', '').strip() if a.select_one(title) else titulos if titulos else ""
                        )
                    coki=getBody(linkedin+a.select_one(href).get("href").replace('\\n', ' ').replace('\\r', '').strip(),content=content,imajin=imajina)
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
    return date2.strftime('%%Y-%%m-%%d %%H:%%M:%%S')
def compareDate(dates,lastDate):
    dt = parse(dates.strip())
    dateCompare = date(2020, 6, 1)  
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared


""" % (str(numba),str(numba),name,pr)
    return popo2
numba=71
for a in ta:
    name=""
    pr=""
    if a[2]=="rss":
        name=a[0]
        pr=a[1]
        capin=golek(numba,name,pr)
        f = open("all_link/link%s.py" % (numba), "a")
        f.write(capin)
        f.close()
    elif a[2]=="page":
        name=a[0]
        pr=a[1]
        capin=golek1(numba,name,pr)
        f = open("all_link/link%s.py" % (numba), "a")
        f.write(capin)
        f.close()
    else:
        name=a[0]
        pr=a[1]
        capin=golek2(numba,name,pr)
        f = open("all_link/link%s.py" % (numba), "a")
        f.write(capin)
        f.close()
    numba+=1





