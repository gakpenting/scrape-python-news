import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from mysqls.pandasql import Links
def link10():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 10 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Ealing",Links.LA_pr=="https://ealingnewsextra.co.uk/category/latest-news/").order_by(Links.date.desc())
        while True:
            namber=str(number)
            setop=False
            link='https://ealingnewsextra.co.uk/category/latest-news/page/'+namber
            r = requests.get(link, timeout=5)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select(".tn-module5-wrap")
            
            for a in lista[::-1]:
                s=a.select_one("time").getText()
                # print(compareDate(s,lastDate))
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                         LA_name="Ealing",
                LA_pr="https://ealingnewsextra.co.uk/category/latest-news/", 
                                          date=getDate(s),
                                          title=a.select_one("a").get("title")                        
                        )
                    papa.body=getBody(a.select_one("a").get("href"))
                    papa.image=a.select_one("img").get("src")
                    papa.save()
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 10", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = parse(dates.strip())
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dateCompare = date(2020, 6, 1)
    lastDate=Links.select().order_by(Links.date.desc())
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)
    dt = parse(dates.strip())
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getBody(link):
    try:
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.single-post-content').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""