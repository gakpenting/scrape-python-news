import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link17():
    getList()

def getList():
    pa=[]
    number=0
    
    try:
        print("link 17 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Slough",Links.LA_pr=="https://slough.gov.uk/news/").order_by(Links.date.desc())
        link='https://slough.gov.uk/news/rss/news.ashx'
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
        
        for a in lista[::-1]:
            s=a.select_one("pubDate")
            # print(compareDate(s.getText(),lastDate))
            # print(a.select_one("link").getText())
            image=''
            title=a.select_one("title").getText()
            if compareDate(s.getText(),lastDate):
                papa,created=Links.get_or_create(
                    LA_name="Slough",
                LA_pr="https://slough.gov.uk/news/",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=getBody(a.select_one("link").getText())
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 17 ", str(e) )
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
        panda=soup.select_one('div.articleContent').getText()
        
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""
