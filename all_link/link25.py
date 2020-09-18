import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link25():
    getList()
   

def getList():
    pa=[]
    number=0
    
    try:
        print("link 25 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="South Cambridgeshire",Links.LA_pr=="https://www.scambs.gov.uk/news/").order_by(Links.date.desc())
        link='https://www.scambs.gov.uk/news/'
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        lista=soup.select("div.news-archive > div.row")
        #
        
        for a in lista[::-1]:
            s=getBody("https://www.scambs.gov.uk"+a.select_one("a").get("href"))
            # print(s[0])
            # print(compareDate(s[0],lastDate))
            # print("https://www.scambs.gov.uk"+a.select_one("a").get("href"))
            
            
            title=a.select_one("h3").getText().replace('\n', ' ').replace('\r', '').strip()
            if compareDate(s[0],lastDate):
                papa,created=Links.get_or_create(
                    LA_name="South Cambridgeshire",
                LA_pr="https://www.scambs.gov.uk/news/",
                                        date=getDate(s[0]),
                                        title=title                    
                    )
                papa.body=s[1]
                papa.image=s[2]
                papa.save()
                
    except Exception as e:
        print("err link 25 ", str(e) )
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
    cabi=""
    try:
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        tabi=soup.select("div.container")[1].select_one("p").getText().replace("News release from","").replace('\n', ' ').replace('\r', '').strip() if soup.select_one(".container") else ""
        imag=soup.select("div.container")[1].select("img")
        tumi=soup.select("div.container")[1].select_one("div.mt-4").getText().replace('\n', ' ').replace('\r', '').strip()
        for a in imag:
            cabi+="https://www.scambs.gov.uk"+a.get("src")+"|"
        return [tabi,tumi,cabi]
     
    except:
        return [tabi,tumi,cabi]
