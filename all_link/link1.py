import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links

def link1():
    try:
        # 1. http://www.stevenage.gov.uk/news-and-events/news/
        data=[]
        r = requests.get('http://www.stevenage.gov.uk/news-and-events/news/', timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.ItemList')
        panda1=panda.select_one("ul")
        panda2=panda1.select("li")
        b=0
        print("link 1 start scraping...")
        
        lastDate=Links.select().where(Links.LA_name=="Stevenage",Links.LA_pr=="http://www.stevenage.gov.uk/news-and-events/news/").order_by(Links.date.desc())
        # print(len(panda2))
        for a in panda2[::-1]:
            b+=1
            dt = datetime.strptime(a.select_one("span").getText().strip(), '%d %b %Y')
            dateCompare = date(2020, 6, 1)    
            
            if len(lastDate)>0:
                dateLen=lastDate[0].date
                dateCompare=date(dateLen.year,dateLen.month,dateLen.day)
            date2 = date(dt.year, dt.month, dt.day)
            dateCompared = date2 > dateCompare    
            # print(a.select_one("a").get("title"))      
            
            if dateCompared == True:
                
                papa,created=Links.get_or_create(LA_name="Stevenage",
                LA_pr="http://www.stevenage.gov.uk/news-and-events/news/",
                title=a.select_one("a").get("title"),
                date=date2.strftime('%Y-%m-%d %H:%M:%S'),
                
                )
                lopo=getBody("http://www.stevenage.gov.uk"+a.select_one("a").get("href"),0)
                copo=papa.body if lopo == '' or lopo == None else lopo
                papa.image=getImage("http://www.stevenage.gov.uk"+a.select_one("a").get("href"),0)
                papa.body=copo
                papa.save()
        
        # return data
    except Exception as e:
        print("link 1 error",str(e))
def getImage(link,cupid):
    print(cupid)
    cupid+=1
    try:
        print(link)
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one("div#ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_StandardNewsPage_lblBody").select_one('img').get("src")
        return panda
     
    except Exception as e:
        print(str(e))
        return ""
def getBody(link,cupid):
    # print(cupid)
    cupid+=1
    try:
        print(link)
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div#ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_StandardNewsPage_lblBody').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except Exception as e:
        if cupid != 10:
            return getBody(link,cupid)
            
        else:
            print(str(e))
            return ""