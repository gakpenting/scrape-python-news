import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link23():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    
    try:
        print("link 23 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Wycombe",Links.LA_pr=="https://www.wycombe.gov.uk/News/All-news.aspx").order_by(Links.date.desc())
        link='https://www.wycombe.gov.uk/News/All-news.aspx?Listing_SyndicationType=1'
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
        
        for a in lista[::-1]:
            s=a.select_one("pubDate")
            # print(compareDate(s.getText(),lastDate))
            # print(a.select_one("link").getText())
            image=a.select_one("thumbnail").get("url") if a.select_one("thumbnail") else ""
            title=a.select_one("title").getText()
            if compareDate(s.getText(),lastDate):
                papa,created=Links.get_or_create(
                    LA_name="Wycombe",
                LA_pr="https://www.wycombe.gov.uk/News/All-news.aspx",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=getBody(a.select_one("content").get("url")) if a.select_one("content") else ""
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 23 ", str(e) )
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
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser').getText()
        return soup.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""
