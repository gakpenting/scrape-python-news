import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link22():
    getList()

def getList():
    pa=[]
    number=1
    try:
        print("link 22 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Milton Keynes",Links.LA_pr=="https://www.milton-keynes.gov.uk/").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://www.milton-keynes.gov.uk/pressreleases/2020?page='+namber
            r = requests.get(link, timeout=15,verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("article")
         
            for a in lista[::-1]:
                s=a.select_one("p").getText()
                # print(s)
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Milton Keynes",
                        LA_pr="https://www.milton-keynes.gov.uk/",
                        date=getDate(s),                        
                        title=a.select_one("a").getText()
                        )
                    cupid=getBody("https://www.milton-keynes.gov.uk"+a.select_one("a").get("href"))
                    papa.body=cupid[0]
                    papa.image=cupid[1]
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 22 ", str(e) )
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
    image=""
    text=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one('div.content.right').getText().replace('\n', ' ').replace('\r', '').strip()
        image="https://www.milton-keynes.gov.uk"+soup.select_one('.contentImg').select_one("img").get("src") if soup.select_one('.contentImg') else ""
        text=panda1
        return [text,image]
     
    except:
        return [text,image]