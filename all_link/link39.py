import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link39():
    getList()

def getList():
    pa=[]
    number=1
    try:
        print("link 39 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Chesterfield",Links.LA_pr=="https://www.chesterfield.gov.uk/home/latest-news.aspx").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://www.chesterfield.gov.uk/home/latest-news.aspx?page='+namber
            r = requests.get(link, timeout=15,verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("ul.media-list.news-teaser-list")
            if len(lista) == 0:
                break
            # print(lista[0])
            

            for a in lista[::-1]:
                s=a.select_one("small.muted").getText().replace("Published on ","")
                # print(s)
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Chesterfield",
                        LA_pr="https://www.chesterfield.gov.uk/home/latest-news.aspx",
                        date=getDate(s),                        
                        title=a.select_one("h2.media-heading").getText().replace('\n', ' ').replace('\r', '').strip()
                        )
                    coki=getBody("https://www.chesterfield.gov.uk"+a.select_one("a").get("href"))
                    papa.body=coki[0]
                    papa.image=coki[1]
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 39 ", str(e) )
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
    panda1=""
    image=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a=soup.select("div.media-body p")
        s=""
        for j in a:
            s+=j.getText().strip()
        panda1=s
        
        
        return [panda1,image]
     
    except:
        return [panda1,image]