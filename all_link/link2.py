import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
def link2():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 2 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Greater London",Links.LA_pr=="https://www.london.gov.uk/media-centre").order_by(Links.date.desc())
        while True:
            namber=str(number)
            setop=False
            link='https://www.london.gov.uk/media-centre/mayors-press-releases?order=DESC&page='+namber
            r = requests.get(link, timeout=5)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("article.node.node--press-release.node--dynamic-teaser")
                     
            for a in lista[::-1]:
                s=a.select_one(".date-display-single")
                print(compareDate(s.getText(),lastDate))
                print(a.select_one("a").get("href"))
                if compareDate(s.getText(),lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Greater London",
                LA_pr="https://www.london.gov.uk/media-centre",
                        date=getDate(s.getText()),
                        title=a.select_one("a").get("title"),
                        image=''
                        )
                    papa.body=getBody('https://www.london.gov.uk'+a.select_one("a").get("href"))
                    papa.save()
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("link 2 error ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates, '%d %B %Y')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = datetime.strptime(dates, '%d %B %Y')
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
        panda=soup.select_one('div.content').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return "error"