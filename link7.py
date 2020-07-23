import requests
from datetime import datetime,date
from bs4 import BeautifulSoup

def link7():
    return getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    
    try:
        link='https://www.bromley.gov.uk/rss/news'
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
        
        for a in lista:
            s=a.select_one("pubDate")
            print(compareDate(s.getText()))
            print(a.select_one("link").getText())
            image=''
            title=a.select_one("title").getText()
            if compareDate(s.getText()):
                pa.append(putData(
                    main_link="https://www.bromley.gov.uk",
                    link=link,
                    source=a.select_one("link").getText(),
                    title=title,
                    date=getDate(s.getText()),
                    body=getBody(a.select_one("link").getText()),
                    image=image,
                    ))
                
    except Exception as e:
        print("err ", str(e) )
        return pa
    return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates.strip(), '%a, %d %b %Y %H:%M:%S %z')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates):
    dt = datetime.strptime(dates.strip(), '%a, %d %b %Y %H:%M:%S %z')
    dateCompare = date(2020, 6, 1)    
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared

def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('#main-content > div.main-left.column.span-8').select_one("a").get("href")
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('#main-content > div.main-left.column.span-8 > div').getText()
        return panda
     
    except:
        return ""
def getDateBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('p.lead.text-muted').getText()
        return panda
     
    except:
        return "1 June 2020"