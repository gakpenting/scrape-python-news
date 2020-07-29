import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
def link5():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 5 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Bexley",Links.LA_pr=="https://www.bexley.gov.uk/news").order_by(Links.date.desc())
        while True:
            namber=str(number)
            setop=False
            link='https://www.bexley.gov.uk/news?field_news_category_target_id=All&page='+namber
            r = requests.get(link, timeout=5)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("div.col-xs-12.views-row")
            
            for a in lista[::-1]:
                s=a.select_one("span.field-content")
                # print(compareDate(s.getText(),lastDate))
                # print(a.select_one("a").get("href"))
                image=''
                copin=getImage('https://www.bexley.gov.uk'+a.select_one("a").get("href"))
                if copin:
                    image='https://www.bexley.gov.uk'+copin
                if compareDate(s.getText(),lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Bexley",
                LA_pr="https://www.bexley.gov.uk/news",
                        date=getDate(s.getText()),
                        title=a.select_one("a").getText()
                        
                        )
                    papa.body=getBody('https://www.bexley.gov.uk'+a.select_one("a").get("href"))
                    papa.image=image
                    papa.save()
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 5 ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates.strip(), '%d %B, %A, %Y - %H:%M %p')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = datetime.strptime(dates.strip(), '%d %B, %A, %Y - %H:%M %p')
    dateCompare = date(2020, 6, 1)    
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getImage(link):
    try:
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('.bs-region--main').select_one("img").get("src")
        return panda
     
    except:
        return False
def getBody(link):
    try:
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('.bs-region--main').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""