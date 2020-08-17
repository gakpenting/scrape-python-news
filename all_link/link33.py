import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link33():
    getList()

def getList():
    pa=[]
    number=1
    try:
        print("link 33 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Barrow-in-Furness",Links.LA_pr=="https://www.barrowbc.gov.uk/news/tribute-to-councillor-rory-mcclure/").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://www.barrowbc.gov.uk/news/?lister50879p='+namber
            r = requests.get(link, timeout=15,verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("div.newslist ul li")
            if len(lista) == 0:
                break
            # print(lista[0])
            # exit()

            for a in lista[::-1]:
                s=a.select_one("span.oBoxItemDate.item-date").getText()
                # print(s)
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Barrow-in-Furness",
                        LA_pr="https://www.barrowbc.gov.uk/news/tribute-to-councillor-rory-mcclure/",
                        date=getDate(s),                        
                        title=a.select_one(".oBoxItemTitle.item-title").getText()
                        )
                    papa.body=getBody("https://www.barrowbc.gov.uk"+a.select_one("a").get("href"))
                    papa.image="https://www.barrowbc.gov.uk"+a.select_one("img").get("src") if a.select_one("img") else ""
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 33 ", str(e) )
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
    panda1=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one("div#-ux-content div.contenteditor").getText().replace('\n', ' ').replace('\r', '').strip()
        
        return panda1
     
    except:
        return panda1