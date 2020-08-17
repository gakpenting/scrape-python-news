import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link21():
    getList()

def getList():
    pa=[]
    number=1
    try:
        print("link 21 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Aylesbury Vale",Links.LA_pr=="https://www.aylesburyvaledc.gov.uk/news").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://www.aylesburyvaledc.gov.uk/news?page='+namber
            r = requests.get(link, timeout=15,verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select_one("div.view.view-news").select_one("div.view-content").select("div.views-row")
            if len(lista) == 0:
                break
            for a in lista[::-1]:
                s=a.select_one("h5.field-content").getText()
                # print(s)
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Aylesbury Vale",
                        LA_pr="https://www.aylesburyvaledc.gov.uk/news",
                        date=getDate(s),                        
                        title=a.select_one("a").getText()
                        )
                    cupid=getBody(a.select_one("a").get("href"))
                    papa.body=cupid[0]
                    papa.image=cupid[1]
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 21 ", str(e) )
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
        panda1=soup.select_one('div.field.field-name-field-news-description').getText().replace('\n', ' ').replace('\r', '').strip()
        image=soup.select_one('img.img-responsive').get("src") if soup.select_one('img.img-responsive') else ""
        text=panda1
        return [text,image]
     
    except:
        return [text,image]