import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
def link11():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 11 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="West Oxfordshire",Links.LA_pr=="westoxon.gov.uk/news").order_by(Links.date.desc())
        while True:
            namber=str(number)
            setop=False
            link='https://news.westoxon.gov.uk/news?page='+namber
            r = requests.get(link, timeout=5)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("div.cell.cell-contained.no-padding")
            if len(lista) == 0:
                break 
            for a in lista[::-1]:
                s=a.select_one("p.date")
                # print(compareDate(s.getText().strip(),lastDate))
                # print(a.select_one("a").get("title"))
                if compareDate(s.getText().strip(),lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="West Oxfordshire",
                        LA_pr="westoxon.gov.uk/news",
                        date=getDate(s.getText().strip()),
                        title=a.select_one("a").get("title")                        
                        )
                    papa.image=a.select_one("img").get("src")
                    papa.body=getBody('https://news.westoxon.gov.uk'+a.select_one("a").get("href"))
                    papa.save()
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("link 11 error ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates, '%d %b %Y')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = datetime.strptime(dates, '%d %b %Y')
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
        panda=soup.select_one('div.content-summary').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return ""