import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link40():
    try:
        # 1. http://www.stevenage.gov.uk/news-and-events/news/
        data=[]
        r = requests.get('https://www.derbyshiredales.gov.uk/your-council/news-and-publications/latest-news', timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select('div.blogtoplevelcategory div.blog-panel-item')
        b=0
        print("link 40 start scraping...")
        
        lastDate=Links.select().where(Links.LA_name=="Derbyshire Dales",Links.LA_pr=="https://www.derbyshiredales.gov.uk/your-council/news-and-publications/latest-news").order_by(Links.date.desc())
        # print(len(panda2))
        for a in panda:
            b+=1
            dt = parse(a.select_one("time").getText())
            dateCompare = date(2020, 6, 1)    
            
            if len(lastDate)>0:
                dateLen=lastDate[0].date
                dateCompare=date(dateLen.year,dateLen.month,dateLen.day)
            date2 = date(dt.year, dt.month, dt.day)
            dateCompared = date2 > dateCompare    
            # print(a.select_one("a").get("title"))      
            
            if dateCompared == True:
                
                papa,created=Links.get_or_create(LA_name="Derbyshire Dales",
                LA_pr="https://www.derbyshiredales.gov.uk/your-council/news-and-publications/latest-news",
                title=a.select_one("a.item-title").getText().strip(),
                date=date2.strftime('%Y-%m-%d %H:%M:%S'),
                
                )
                papa.image="https://www.derbyshiredales.gov.uk"+a.select_one("img").get("src") if a.select_one("img") else ""
                papa.body=getBody("https://www.derbyshiredales.gov.uk"+a.select_one("div.item-title a").get("href"),0)
                papa.save()
            else:
                break
        
        # return data
    except Exception as e:
        print("link 40 error",str(e))

def getBody(link,cupid):
    # print(cupid)
    cupid+=1
    try:
        # print(link)
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('section.article-content').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except Exception as e:
        if cupid != 10:
            return getBody(link,cupid)
            
        else:
            print(str(e))
            return ""