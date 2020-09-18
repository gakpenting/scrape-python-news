import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link38():
    try:
        # 1. http://www.stevenage.gov.uk/news-and-events/news/
        data=[]
        r = requests.get('https://www.bolsover.gov.uk/index.php/your-council/latest-news', timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select('li.accordion-item')
        b=0
        print("link 38 start scraping...")
        
        lastDate=Links.select().where(Links.LA_name=="Bolsover",Links.LA_pr=="https://www.bolsover.gov.uk/index.php/your-council/latest-news").order_by(Links.date.desc())
        # print(len(panda2))
        for a in panda:
            b+=1
            dt = parse(a.select_one("div.fpmoddate").getText())
            dateCompare = date(2020, 6, 1)    
            
            if len(lastDate)>0:
                dateLen=lastDate[0].date
                dateCompare=date(dateLen.year,dateLen.month,dateLen.day)
            date2 = date(dt.year, dt.month, dt.day)
            dateCompared = date2 > dateCompare    
            # print(a.select_one("a").get("title"))      
            
            if dateCompared == True:
                
                papa,created=Links.get_or_create(LA_name="Bolsover",
                LA_pr="https://www.bolsover.gov.uk/index.php/your-council/latest-news",
                title=a.select_one("a").getText().strip(),
                date=date2.strftime('%Y-%m-%d %H:%M:%S'),
                
                )
                papa.image=""
                papa.body=a.select_one("div.acc-content").getText()
                papa.save()
        
        # return data
    except Exception as e:
        print("link 38 error",str(e))

def getBody(link,cupid):
    # print(cupid)
    cupid+=1
    try:
        # print(link)
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.bodyText').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except Exception as e:
        if cupid != 10:
            return getBody(link,cupid)
            
        else:
            print(str(e))
            return ""