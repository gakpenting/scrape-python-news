import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link24():
    getList()
   

def getList():
    pa=[]
    number=0
    
    try:
        print("link 24 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="East Cambridgeshire",Links.LA_pr=="https://www.eastcambs.gov.uk/content/press-releases").order_by(Links.date.desc())
        link='https://www.eastcambs.gov.uk/feed/latest-press-releases.xml'
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'lxml-xml')
        lista=soup.select("item")
        
        for a in lista[::-1]:
            s=a.select_one("pubDate")
            # print(compareDate(s.getText(),lastDate))
            # print(a.select_one("link").getText())
            
            title=a.select_one("title").getText()
            if compareDate(s.getText(),lastDate):
                papa,created=Links.get_or_create(
                    LA_name="East Cambridgeshire",
                LA_pr="https://www.eastcambs.gov.uk/content/press-releases",
                                        date=getDate(s.getText()),
                                        title=title                    
                    )
                capin=getBody(a.select_one("link").getText())
                papa.body=capin[0]
                papa.image=capin[1]
                papa.save()
                
    except Exception as e:
        print("err link 24 ", str(e) )
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
    tabi=""
    tumi=""
    try:
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        tabi=soup.select_one("div.field-item.even[property='content:encoded']").getText().replace('\n', ' ').replace('\r', '').strip() if soup.select_one("div.field-item.even[property='content:encoded']") else ""
        imag=soup.select("div.field-item > p > img")
        for a in imag:
            tumi+="https://www.eastcambs.gov.uk"+a.get("src")+"|"
        return [tabi,tumi]
     
    except:
        return [tabi,tumi]
