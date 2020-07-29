import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from mysqls.pandasql import Links
def link15():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    
    try:
        print("link 15 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Central Bedfordshire",Links.LA_pr=="https://www.centralbedfordshire.gov.uk/news").order_by(Links.date.desc())
        link='https://www.centralbedfordshire.gov.uk/rss/news'
        r = requests.get(link, timeout=5)
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
                    LA_name="Central Bedfordshire",
                LA_pr="https://www.centralbedfordshire.gov.uk/news",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=getBody(a.select_one("description").getText())
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 15 ", str(e) )
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
        # for cd in soup.findAll(text=True):
        #     if isinstance(cd, CData):
        #         panda+=cd
        
        return panda.replace('\n', ' ').replace('\r', '').strip()
        
     
    except:
        return ""
