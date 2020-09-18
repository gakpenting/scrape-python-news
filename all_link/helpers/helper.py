import requests
from datetime import datetime,date,timedelta 
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import re
def getDate(link=None,date="sam",replaceDate=None,replaceRegex=None):
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1="1 January 2020"
        panda1=soup.select_one(date).getText() if soup.select_one(date) else "1 January 2020"
        # print(panda1)
        if replaceRegex:
            cop=re.search(replaceRegex, soup.select_one(date).getText())
            panda1=cop.group() if cop else "1 January 2020"
            # print(panda1)
        if replaceDate:
            panda1=soup.select_one(date).getText().replace(replaceDate,"") if soup.select_one(date) else "1 January 2020"
                    
        if soup.select_one(date):
            if soup.select_one(date).name == "meta":
                panda1=soup.select_one(date).get("content")
        
        return panda1
     
    except:
        
        return "1 January 2020"
def getBody(link,content="sam",imajin="sam",linkedin2=""):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        
        panda=soup.select(content) if soup.select(content) else []
        
        # print(soup)
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        image=soup.select(imajin) if soup.select(imajin) else []
        # print(soup)
        tabi=""
        if len(image)> 1:
            for a in image:
                tabi+=linkedin2+a.get("src")+"|"
            image=tabi
        else:
            image=linkedin2+soup.select_one(imajin).get("src") if soup.select_one(imajin) else ""
        return [panda1,image]
     
    except Exception as e:
        print(str(e))
        return [panda1,image]

def getTitle(link,title="sam"):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        
        panda1=soup.select(title) if soup.select(title) else ""
        
        return panda1
     
    except Exception as e:
        print(str(e))
        return panda1