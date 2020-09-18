import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link20():
    getList()

def getList():
    pa=[]
    number=1
    try:
        print("link 20 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Buckinghamshire",Links.LA_pr=="https://www.buckscc.gov.uk/news/").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://www.buckscc.gov.uk/news/?page='+namber
            r = requests.get(link, timeout=15)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("li.thumbnail-wrapper")
            if len(lista) == 0:
                break
            # print(len(lista))
            
            for a in lista[::-1]:
                s=a.select_one("li.list-group-item.thumbnail-date-caption").getText()
                # print(s)
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Buckinghamshire",
                        LA_pr="https://www.buckscc.gov.uk/news/",
                        date=getDate(s),                        
                        title=a.select_one("a").getText()
                        )
                    papa.body=getBody(a.select_one("a").get("href"))
                    papa.image="https://www.buckscc.gov.uk"+a.select_one("img").get("src")
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 20 ", str(e) )
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
def getBody(link):
    try:
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one('div.pcg-rte-wrapper').getText()
        return panda1.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""