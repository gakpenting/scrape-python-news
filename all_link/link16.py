import requests
from datetime import datetime,date, timedelta 
from dateutil.parser import parse
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
def link16():
    getList()
    


def getList():
    pa=[]
    lastDate=Links.select().where(Links.LA_name=="Luton",Links.LA_pr=="lutontoday.co.uk/news").order_by(Links.date.desc())
    number=lastDate[0].date if len(lastDate) > 0 else date(2020,6,2)
    
    try:
        print("link 16 start scraping...")
        
        while True:
            namber=number
            link='https://www.lutontoday.co.uk/archive/'+str(namber.year)+'/'+str(namber.month)+'/'+str(namber.day)
            # print(link)
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
            r = requests.get(link, timeout=15,headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            
            lista=soup.select_one("div#frameInner").select_one("div").select_one("ul").select("li")
            
            if not lista:
                # print("po")
                break
            
            for a in lista:
                # print(a.select_one("a").getText())
                if a.select_one("a").get("href").strip() != 'undefined': 
                    sipu=getBodyAndImage("https://www.lutontoday.co.uk"+a.select_one("a").get("href"))
                    papa,created=Links.get_or_create(
                        LA_name="Luton",
                        LA_pr="lutontoday.co.uk/news",
                        date=sipu[0],
                        title=a.select_one("a").getText().strip()                        
                        )
                    
                    papa.image=sipu[1]
                    papa.body=sipu[2]
                    papa.save()
                else:
                    break
                
            number+=timedelta(days=1)
            
    except Exception as e:
        print("link 16 error ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dambo=parse(dates)
    return dambo.strftime('%Y-%m-%d %H:%M:%S')
def getBodyAndImage(link):
    s=""
    image=""
    datess=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        r = requests.get(link, timeout=15,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        dayte=soup.select_one("#frameInner > article > div:nth-of-type(4) > div > div:nth-of-type(2)")
        dayte2=soup.select_one("#frameInner > article > div:nth-of-type(5) > div > div:nth-of-type(2)")
        datess=getDate(dayte.getText()) if dayte else getDate(dayte2.getText())
        
        
        panda=soup.select("#content-wrapper > div.markup")
        
        for z in panda:
            s+=z.getText()
        imajin=soup.select_one("#content-wrapper > div:nth-of-type(1) > figure > amp-img")
        imajin2=soup.select_one("article > div:nth-of-type(4) > div > figure >amp-img")
        image="https://www.lutontoday.co.uk"+imajin.get("src") if imajin else "https://www.lutontoday.co.uk"+imajin2.get("src") if imajin2 else "https://www.lutontoday.co.uk"+soup.select_one("amp-img").get("src")
        return [datess,image,s.replace('\n', ' ').replace('\r', '').strip()]
     
    except Exception as e:
        print("link16 getbodyandimagerr "+str(e))
    #     exit()
        return [s,image,datess]
