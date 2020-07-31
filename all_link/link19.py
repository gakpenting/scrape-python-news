import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link19():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=1
    try:
        print("link 19 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Bristol, City of",Links.LA_pr=="https://news.bristol.gov.uk/news").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://news.bristol.gov.uk/news?page='+namber
            r = requests.get(link, timeout=15)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select(".cell.cell-contained.no-padding")
            # print(len(lista))
            # exit()
            for a in lista[::-1]:
                s=a.select_one("p.date").getText()
                # print(s)
                # print(a.select_one("a").get("title"))
                # exit()
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Bristol, City of",
                LA_pr="https://news.bristol.gov.uk/news",
                        date=getDate(s),                        
                        title=a.select_one("a").get("title")
                        )
                    papa.body=getBody('https://news.bristol.gov.uk'+a.select_one("a").get("href"))
                    papa.image=a.select_one("img").get("src")
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 19 ", str(e) )
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
        panda1=soup.select_one('div.content-summary').getText()
        panda=soup.select_one('div.content-body').getText()
        return panda1.replace('\n', ' ').replace('\r', '').strip()+panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""