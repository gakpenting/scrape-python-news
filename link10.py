import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from pandasql import Links
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
        while True:
            namber=str(number)
            setop=False
            link='https://ealingnewsextra.co.uk/category/latest-news/page/'+namber
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select(".tn-module5-wrap")
            
            for a in lista:
                s=a.select_one("time").getText()
                print(compareDate(s))
                print(a.select_one("a").get("href"))
                if compareDate(s):
                    papa,created=Links.get_or_create(
                        main_link="https://ealingnewsextra.co.uk",
                                          date=getDate(s),
                                          title=a.select_one("a").get("title")                        
                        )
                    papa.body=getBody(a.select_one("a").get("href"))
                    papa.image=a.select_one("img").get("src")
                    papa.link=link
                    papa.source=a.select_one("a").get("href")
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
def compareDate(dates):
    dt = parse(dates.strip())
    dateCompare = date(2020, 6, 1)    
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.single-post-content').getText()
        return panda
     
    except:
        return ""