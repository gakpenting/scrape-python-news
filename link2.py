import requests
from datetime import datetime,date
from bs4 import BeautifulSoup

def link2():
    return getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        while True:
            namber=str(number)
            setop=False
            link='https://www.london.gov.uk/media-centre/mayors-press-releases?order=DESC&page='+namber
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("article.node.node--press-release.node--dynamic-teaser")
                     
            for a in lista:
                s=a.select_one(".date-display-single")
                print(compareDate(s.getText()))
                print(a.select_one("a").get("href"))
                if compareDate(s.getText()):
                    pa.append(putData(
                        main_link="https://www.london.gov.uk",
                        link=link,
                        source=a.select_one("a").get("href"),
                        title=a.select_one("a").get("title"),
                        date=getDate(s.getText()),
                        body=getBody('https://www.london.gov.uk'+a.select_one("a").get("href")),
                        image='',
                        ))
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err ", str(e) )
        return pa
    return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates, '%d %B %Y')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates):
    dt = datetime.strptime(dates, '%d %B %Y')
    dateCompare = date(2020, 6, 1)    
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('div.content').getText()
        return panda
     
    except:
        return "error"