import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from pandasql import Links
def link4():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 4 start scraping...")
        while True:
            namber=str(number)
            setop=False
            link='https://www.barnet.gov.uk/news?page='+namber
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("li.result")
            
            for a in lista:
                s=a.select_one(".item-date")
                print(compareDate(s.getText().replace("Last updated: ", "")))
                print(a.select_one("a").get("href"))
                if compareDate(s.getText().replace("Last updated: ", "")):
                    papa,created=Links.get_or_create(
                        LA_name="Barnet",
                LA_pr="https://www.barnet.gov.uk/news",
                        date=getDate(s.getText().replace("Last updated: ", "")),                        
                        title=a.select_one("a").getText()
                        )
                    papa.body=getBody('https://www.barnet.gov.uk'+a.select_one("a").get("href"))
                    papa.image='https://www.barnet.gov.uk'+a.select_one("img").get("src")
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 4 ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = datetime.strptime(dates.strip(), '%d %B, %Y')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates):
    dt = datetime.strptime(dates.strip(), '%d %B, %Y')
    dateCompare = date(2020, 6, 1)    
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('article').getText()
        return panda.replace('\n', ' ').replace('\r', '').strip()
     
    except:
        return "error"