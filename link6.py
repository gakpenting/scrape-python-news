import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from pandasql import Links
def link6():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    capin=1
    try:
        print("link 6 start scraping...")
        while True:
            
            tobi=capin*10
            setop=False
            link='https://www.brent.gov.uk/news?count='+str(tobi)
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select_one(".newsEventsList").find_all(recursive=False)
           
            for a in lista[(capin - 1) * 10:capin * 10]:
                s="1 June 2020"
                if a.select_one("a"):
                    s=getDateBody(a.select_one("a").get("href"))
                else:
                    s=getDateBody(a.get("href"))
                print(compareDate(s))
                print(a.select_one("a").get("href") if a.select_one("a") else a.get("href"))
                image=''
                title=''
                if a.select_one(".news_article_image"): 
                    image="https://www.brent.gov.uk"+a.select_one(".news_article_image").get("style").replace("background-image:url('","").replace("');","")
                if a.select_one("h3.mb-1"):
                    title=a.select_one("h3.mb-1").getText()
                elif a.select_one("a"):
                    title=a.select_one("a").getText()
                if compareDate(s):
                    papa,created=Links.get_or_create(
                        main_link="https://www.brent.gov.uk",
                                             date=getDate(s),
                                             title=title
                        )
                    papa.link=link,
                    papa.source=a.select_one("a").get("href") if a.select_one("a") else a.get("href")
                    papa.body=getBody('https://www.brent.gov.uk'+a.select_one("a").get("href") if a.select_one("a") else a.get("href"))
                    papa.image=image
                    papa.save()
                else:
                    setop=True
            if setop:
                break
            capin+=1
    except Exception as e:
        print("err link 6", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates.strip(), '%d %B %Y')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates):
    dt = datetime.strptime(dates.strip(), '%d %B %Y')
    dateCompare = date(2020, 6, 1)    
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared

def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('article').getText()
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