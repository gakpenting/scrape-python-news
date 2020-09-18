import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from mysqls.pandasql import Links
def link32():
    getList()
    


def getList():
    pa=[]
    number=0
    
    try:
        print("link 32 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Cumbria",Links.LA_pr=="http://www.yourcumbria.org/News/").order_by(Links.date.desc())
        link='http://www.yourcumbria.org/rss/All/'
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
              
        for a in lista:
            s=a.select_one("pubDate")
            # print(compareDate(s.getText(),lastDate))
            # print(s)
            image = BeautifulSoup(a.select_one("description").string, 'html.parser').select_one("img").get("src") if BeautifulSoup(a.select_one("description").string, 'html.parser').select_one("img") else ""
            cabang=getImageAndBody(a.select_one("link").getText())
            title=a.select_one("title").getText()
            if compareDate(s.getText(),lastDate):
                papa,created=Links.get_or_create(
                    LA_name="Cumbria",
                LA_pr="http://www.yourcumbria.org/News/",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=cabang
                papa.image=image
                papa.save()
            else:
                break
                
    except Exception as e:
        print("err link 32 ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt =parse(dates.strip())
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt =parse(dates.strip())
    dateCompare = date(2020, 6, 1)    
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getImageAndBody(link):
    
    body=""
    try:
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text,'html.parser')
        capin=soup.select("div#PageContent p") if len(soup.select("div#PageContent p"))>0 else soup.select("div#PageContent div")
        ca=""
        for a in capin:
            ca+=a.getText()
        body=ca
        return body
        
     
    except:
        return body
