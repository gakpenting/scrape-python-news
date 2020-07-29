import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
def link13():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    
    try:
        print("link 13 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Waverley",Links.LA_pr=="waverley.gov.uk/news").order_by(Links.date.desc())
        link='https://waverley.gov.uk/rss/news'
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
                    LA_name="Waverley",
                LA_pr="waverley.gov.uk/news",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                papa.body=getBody(a.select_one("link").getText())
                papa.image=image
                papa.save()
                
    except Exception as e:
        print("err link 13 ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates.strip(), '%a, %d %b %Y %H:%M:%S %z')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = datetime.strptime(dates.strip(), '%a, %d %b %Y %H:%M:%S %z')
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
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('article > p > strong').getText()
        panda2=soup.select_one('div.editor').getText().replace('\n', ' ').replace('\r', '').strip()
        return panda.replace('\n', ' ').replace('\r', '').strip()+panda2
     
    except:
        return ""
def getDateBody(link):
    try:
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('p.lead.text-muted').getText()
        return panda
     
    except:
        return "1 June 2020"