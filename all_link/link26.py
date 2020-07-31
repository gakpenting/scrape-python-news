import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link26():
    getList()

def getList():
    pa=[]
    number=1
    try:
        print("link 26 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Cheshire East",Links.LA_pr=="https://www.cheshireeast.gov.uk/council_and_democracy/council_information/media_hub/media_releases/media-releases.aspx").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://www.cheshireeast.gov.uk/council_and_democracy/council_information/media_hub/media_releases/media-releases.aspx?GenericListMediaMasterList_List_GoToPage='+namber
            r = requests.get(link, timeout=15)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("ul.sys_itemslist > li:nth-child(1)")
            # print(lista[10])
            # exit()
            for a in lista[::-1]:
                s=a.select_one("b").getText().split("-")[1].replace('\n', ' ').replace('\r', '').strip()
                
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Cheshire East",
                        LA_pr="https://www.cheshireeast.gov.uk/council_and_democracy/council_information/media_hub/media_releases/media-releases.aspx",
                        date=getDate(s),                        
                        title=a.select_one("a").getText()
                        )
                    lamda=getBody("https://www.cheshireeast.gov.uk"+a.select_one("a").get("href"))
                    papa.body=lamda[0]
                    papa.image=lamda[1]
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 26 ", str(e) )
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
    tobi=""
    tambun=""
    try:
        r = requests.get(link, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('main#mainContent').select("p")
        imajin=soup.select_one('main#mainContent').select("img")
        for a in panda:
            tobi+=a.getText().replace('\n', ' ').replace('\r', '').strip()
        for j in imajin:
            tambun+="https://www.cheshireeast.gov.uk"+j.get("src")+"|"
        return [tobi,tambun]
     
    except:
        return [tobi,tambun]