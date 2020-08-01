import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from mysqls.pandasql import Links
def link29():
    getList()
    


def getList():
    pa=[]
    number=0
    
    try:
        print("link 29 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Cornwall",Links.LA_pr=="https://www.cornwall.gov.uk/council-and-democracy/council-news-room/").order_by(Links.date.desc())
        link='https://www.cornwall.gov.uk/rss-feeds/newsfeed/'
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
        
        for a in lista[::-1]:
            s=a.select_one("pubDate")
            # print(compareDate(s.getText(),lastDate))
            # print(a.select_one("link").getText())
            image=getImage(a.select_one("link").getText())
            title=a.select_one("title").getText()
            if compareDate(s.getText(),lastDate):
                papa,created=Links.get_or_create(
                    LA_name="Cornwall",
                LA_pr="https://www.cornwall.gov.uk/council-and-democracy/council-news-room/",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=getBody(a.select_one("description").getText())
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 29 ", str(e) )
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

def getBody(link):
    try:
        soup = BeautifulSoup(link,'html.parser')        
        panda=soup.getText()
        
        return panda.replace('\n', ' ').replace('\r', '').strip()
        
     
    except:
        return ""
def getImage(link):
    try:
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text,'html.parser')
        panda="https://www.cornwall.gov.uk"+soup.select_one("div.content-modern img").get("src") if soup.select_one("div.content-modern img") else ""       
        return panda
        
     
    except:
        return ""
