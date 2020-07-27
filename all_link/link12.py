import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
def link12():
    getList()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getList():
    pa=[]
    number=0
    try:
        print("link 12 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Wealden",Links.LA_pr=="wealden.gov.uk/news").order_by(Links.date.desc())
        while True:
            namber=str(number)
            setop=False
            link='https://www.wealden.gov.uk/news/?newsPage='+namber
            r = requests.get(link, timeout=5)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("div.card.w-100.archive-card")
                     
            for a in lista[::-1]:
                s=a.select_one("strong")
                print(compareDate(s.getText().replace("Publish Date:","").strip(),lastDate))
                print(a.select_one("a").getText())
                if compareDate(s.getText().replace("Publish Date:","").strip(),lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Wealden",
                        LA_pr="wealden.gov.uk/news",
                        date=getDate(s.getText().replace("Publish Date:","").strip()),
                        title=a.select_one("a").getText()                        
                        )
                    papa.image=getImage(a.select_one("a").get("href"))
                    papa.body=getBody(a.select_one("a").get("href"))
                    papa.save()
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("link 12 error ", str(e) )
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
        panda=soup.select('strong')[1].getText()
        panda2=soup.select_one('div.news-content').getText().replace('\n', ' ').replace('\r', '').strip()
        return panda.replace('\n', ' ').replace('\r', '').strip()+panda2
     
    except:
        return ""
def getImage(link):
    try:
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('img.news-image').get("src") if soup.select_one('img.news-image') else ''
        return panda
     
    except:
        return ""