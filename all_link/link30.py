import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from mysqls.pandasql import Links
def link30():
    getList()
    


def getList():
    pa=[]
    number=0
    
    try:
        print("link 30 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="County Durham",Links.LA_pr=="https://www.durham.gov.uk/article/1873/News-Events").order_by(Links.date.desc())
        link='https://www.durham.gov.uk/news?format=rss&category=AAP'
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
        
        for a in lista[::-1]:
            s=a.select_one("pubDate")
            # print(compareDate(s.getText(),lastDate))
            # print(a.get("xml:base"))
            cabang=getImageAndBody(a.get("xml:base"))
            image=cabang[0]
            title=a.select_one("title").getText()
            if compareDate(s.getText(),lastDate):
                papa,created=Links.get_or_create(
                    LA_name="County Durham",
                LA_pr="https://www.durham.gov.uk/article/1873/News-Events",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=cabang[1]
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 30 ", str(e) )
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
        body2=soup.select_one("div.a-intro.a-intro--default").getText()
        image=soup.select_one("div.imagecaptioninline img").get("src") if soup.select_one("div.imagecaptioninline img") else ""       
        body=body2+soup.select_one("div.a-body.a-body--default").getText()
        return [image,body]
        
     
    except:
        return [image,body]
