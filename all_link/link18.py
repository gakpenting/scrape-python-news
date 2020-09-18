import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link18():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 18 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Wokingham",Links.LA_pr=="https://news.wokingham.gov.uk/").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://news.wokingham.gov.uk/news/?lister1875p='+namber
            r = requests.get(link, timeout=15,verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select_one(".oBoxList").select("li")
            if len(lista) == 0:
                break
            for a in lista[::-1]:
                s=a.select_one(".oBoxItemDate.item-date").getText()
                # print(s)
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Wokingham",
                LA_pr="https://news.wokingham.gov.uk/",
                        date=getDate(s),                        
                        title=a.select_one("a").getText()
                        )
                    papa.body=getBody('https://news.wokingham.gov.uk'+a.select_one("a").get("href"))
                    papa.image='https://news.wokingham.gov.uk'+a.select_one("img").get("src")
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 18 ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = parse(dates.strip())
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = parse(dates.strip())
    dateCompare = date(2020, 6, 1)  
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getBody(link):
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.contenteditor').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""