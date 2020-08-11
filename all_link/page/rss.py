import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def getList(xmlType="lxml-xml",content="sam",imajina="",numero=None,LA_name=None,LA_pr=None,links=None,listas=None,datesss="pubDate",replaceDate="",titles="title",getBody=None,imajinasi=None,linkedin="",href="link",linkedin2=""):
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        link=links
        r = requests.get(link, timeout=5)
        soup = BeautifulSoup(r.text, xmlType)
        lista=soup.select(listas)
        
        for a in lista:
            s=a.select_one(datesss).getText()
            # print(compareDate(s.getText(),lastDate))
            # print(a.select_one("title").getText())
            image=getBody(linkedin+a.select_one(href).getText().replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina)
            title=a.select_one(titles).getText().replace('\n', ' ').replace('\r', '').strip()
            imajin=linkedin2+a.select_one(imajinasi).getText() if a.select_one(imajinasi) else "" if imajinasi else ""
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                    LA_name=LA_name,
                    LA_pr=LA_pr,
                    date=getDate(s),
                    title=title                    
                    )
                papa.body=image[0] if len(image) > 0 else ""
                papa.image=linkedin2+image[1] if len(image) > 0 and image[1] != "" else imajin
                papa.save()
            else:
                break
                
    except Exception as e:
        print("err link "+numero+" ", str(e) )
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


