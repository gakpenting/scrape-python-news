import requests
from datetime import datetime,date
from dateutil.parser import parse
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
def link14():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 14 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Bedford",Links.LA_pr=="https://www.bedford.gov.uk/news/").order_by(Links.date.desc())
        while True:
            namber=str(number)
            setop=False
            link='https://www.bedford.gov.uk/news/?page='+namber
            r = requests.get(link, timeout=5)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("li.blog-post")
            if len(lista) == 0:
                break
            
            for a in lista[::-1]:
                s=a.select_one("abbr.timeago").getText()
                # print(compareDate(s.strip(),lastDate))
                # print(a.select_one("a").getText())
                if compareDate(s.strip(),lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Bedford",
                        LA_pr="https://www.bedford.gov.uk/news/",
                        date=getDate(s.strip()),
                        title=a.select_one("h2.list-group-item-heading").getText().strip()                        
                        )
                    papa.image=""
                    papa.body=getBody("https://www.bedford.gov.uk"+a.select_one("a").get("href"))
                    papa.save()
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("link 14 error ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt=parse(dates)
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt=parse(dates)
    dateCompare = date(2020, 6, 1)    
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getBody(link):
    try:
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.page-content').getText()
        
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""
