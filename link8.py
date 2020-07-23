import requests
from datetime import datetime,date
from bs4 import BeautifulSoup,CData

def link8():
    return getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    
    try:
        link='https://news.camden.gov.uk/tagfeed/en/tags/headlines,pr'
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
        
        for a in lista:
            s=a.select_one("pubDate")
            print(compareDate(s.getText()))
            print(a.select_one("link").getText())
            image=a.select_one("enclosure").get("url")
            title=a.select_one("title").getText()
            if compareDate(s.getText()):
                pa.append(putData(
                    main_link="https://news.camden.gov.uk",
                    link=link,
                    source=a.select_one("link").getText(),
                    title=title,
                    date=getDate(s.getText()),
                    body=getBody(a.select_one("description").getText()),
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
        soup = BeautifulSoup(link,'html.parser')
        
        panda=soup.getText()
        # for cd in soup.findAll(text=True):
        #     if isinstance(cd, CData):
        #         panda+=cd
        
        return panda
        
     
    except:
        return ""
