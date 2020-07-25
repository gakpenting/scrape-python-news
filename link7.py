import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from pandasql import Links
def link7():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    
    try:
        print("link 7 start scraping...")
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
                papa,created=Links.get_or_create(
                    LA_name="Bromley",
                LA_pr="https://www.bromley.gov.uk/news",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=getBody(a.select_one("link").getText())
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 7 ", str(e) )
        # return pa
    # return pa
        
    

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
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
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