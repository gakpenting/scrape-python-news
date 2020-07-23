import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
def link3():
    return getAll()
    

def putData(main_link=None,link=None,source=None,title=None,date=None,body=None,image=None):
    data={'main_link':main_link,'link':link,'source':source,'title':title,'date':date,'body':body,'image':image}
    return data
def getAll():
    panda=[]
    numba=0
    setop=False
    while True:
        try:
            link="https://www.lbbd.gov.uk/rest/news?_format=json&page="+str(numba)
            r = requests.get(link)
            lista=r.json()["results"]
            for a in lista:
                soup = BeautifulSoup(a["date"], 'html.parser')
                soup2=soup.select_one("time")
                print(compareDate(soup2.getText()))
                print(soup2.getText())
                if compareDate(soup2.getText()):
                    panda.append(putData(
                        main_link="https://www.lbbd.gov.uk",
                        link=link,source=a["path"],title=a["title"]
                    ,date=getDate(soup2.getText())
                    ,body=getBody("https://www.lbbd.gov.uk"+a["path"])
                    ,image="https://www.lbbd.gov.uk"+a["image"]
                    ))
                else:
                    setop=True
            numba+=1
            if setop:
                break
        except:
            break
            print("error")
            return panda
        
                


    # soup = BeautifulSoup(r.text, 'html.parser')
    # lista=soup.select("article.node.node--press-release.node--dynamic-teaser")
    return panda
    

def getDate(dates):
    dt = datetime.strptime(dates, '%A %d %B %Y')
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates):
    dt = datetime.strptime(dates, '%A %d %B %Y')
    dateCompare = date(2020, 6, 1)    
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared
    

def getBody(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select_one('.article--body').getText()
        return panda
     
    except:
        return "error"
