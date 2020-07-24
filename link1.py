import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from pandasql import Links
def link1():
    try:
        # 1. http://www.stevenage.gov.uk/news-and-events/news/
        data=[]
        r = requests.get('http://www.stevenage.gov.uk/news-and-events/news/')
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.ItemList')
        panda1=panda.select_one("ul")
        panda2=panda1.select("li")
        b=0
        print("link 1 start scraping...")
        print(len(panda2))
        for a in panda2:
            b+=1
            dt = datetime.strptime(a.select_one("span").getText().strip(), '%d %b %Y')
            dateCompare = date(2020, 6, 1)    
            date2 = date(dt.year, dt.month, dt.day)
            dateCompared = date2 > dateCompare    
            print(a.select_one("a").get("title"))      
            if dateCompared == True:
                papa,created=Links.get_or_create(main_link="http://www.stevenage.gov.uk",
                title=a.select_one("a").get("title"),
                date=date2.strftime('%Y-%m-%d %H:%M:%S'),
                image=''
                )
                papa.link=a.select_one("a").get("href")
                papa.source='http://www.stevenage.gov.uk/news-and-events/news/'
                papa.body=getBody("http://www.stevenage.gov.uk"+a.select_one("a").get("href"))
                papa.save()
        
        # return data
    except Exception as e:
        print("link 1 error",str(e))

def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.ItemDetails').getText()
        return panda
     
    except:
        return ""