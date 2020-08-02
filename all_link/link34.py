import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from mysqls.pandasql import Links
def link34():
    getList()
    


def getList():
    pa=[]
    number=0
    
    try:
        print("link 34 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Carlisle",Links.LA_pr=="https://www.carlisle.gov.uk/news-and-events").order_by(Links.date.desc())
        link='https://www.carlisle.gov.uk/news-and-events/rss/5196-1'
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.content, features='xml')
        lista=soup.select("item")
        for a in lista[::-1]:
            s=a.select_one("pubDate")
            # print(compareDate(s.getText(),lastDate))
            # print(a.select_one("link"))
            cabang=getImageAndBody(a.select_one("link").getText())
            image=cabang[0]
            title=a.select_one("title").getText()
            if compareDate(s.getText(),lastDate):
                papa,created=Links.get_or_create(
                    LA_name="Carlisle",
                LA_pr="https://www.carlisle.gov.uk/news-and-events",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=cabang[1]
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 34 ", str(e) )
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
    image=""
    body=""
    try:
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text,'html.parser')
        image="https://www.carlisle.gov.uk"+soup.select_one("div.in_article_image img").get("src") if soup.select_one("div.in_article_image img") else ""       
        body=soup.select_one("div.content").getText().replace('\n', ' ').replace('\r', '').strip()
        return [image,body]
        
     
    except:
        return [image,body]
