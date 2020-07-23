import requests
from datetime import datetime,date
from bs4 import BeautifulSoup

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
        print(len(panda2))
        for a in panda2:
            b+=1
            dt = datetime.strptime(a.select_one("span").getText().strip(), '%d %b %Y')
            dateCompare = date(2020, 6, 1)    
            date2 = date(dt.year, dt.month, dt.day)
            dateCompared = date2 > dateCompare          
            if dateCompared == True:
                data.append({'main_link':"http://www.stevenage.gov.uk"
                ,'link':a.select_one("a").get("href")
                ,'source':'http://www.stevenage.gov.uk/news-and-events/news/'
                ,'title':a.select_one("a").get("title")
                ,'date':date2.strftime('%Y-%m-%d %H:%M:%S')
                ,'body':getBody("http://www.stevenage.gov.uk"+a.select_one("a").get("href"))
                ,'image':''
                })
        
        return data
    except:
        print("An exception occurred")

def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.ItemDetails').getText()
        return panda
     
    except:
        return "error"