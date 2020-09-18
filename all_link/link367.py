
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re

def link367():
    getList(
        datea=None,
        content=".content-row",
        imajina="sam",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="367",
        LA_name="Dudley",
        LA_pr="https://www.dudley.gov.uk/news/",
        links="https://www.dudley.gov.uk/news/?currentPage=",
        listas=".article-card",
        datesss="time",
        replaceDate=None,
        title="h3",
        getBody=getBody,
        imajinasi="div > div:nth-child(1) > a > img",
        linkedin="https://www.dudley.gov.uk",
        href="a",
        linkedin2="https://www.dudley.gov.uk",
        
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="367",LA_name="Dudley",LA_pr="https://www.dudley.gov.uk/news/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link=links+namber
            # print(link)
            headers={"Cookie":"TSd9457995075=0402b10008456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1:080f108c5d03200016030882bf3cd6354ab0f1cd11b648211a8099ed8e77e5c4d496f90782b6eb55a00108456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1080f108c5d1098005c466fe9b634dd8c47908baa492b8ffcca6c8f68847f0266ab89ff761209f0944614d490bb192a96207c4218bfcae5ee62d6e8b09a5e01f483e0c11fc435ebd8703f135d9daad70c936849e34569e5ebba5f90dbf6006689ac788a722d285bff4272c33511e1824878e2dc098d76c83abfb470cf4d3ad84d027380cd4de1533eba725f76e4985c5e9e055a9933484853c7f1e444eee287230001000b00008456f7273ab20003312cf6cfbaf7d26fe1dac52d19f0f91a43e45297ccbfc617990e3b3e7f77f7408f88743f00a2800a6a890eb0f9f5bacce875f9e9082faf80bbf66e1be01641bac8f8eab4d69f7e0b682f1e9e553461401000; ASP.NET_SessionId=kojgbtfbklkwg2m3cc31akqp; __RequestVerificationToken=2ZbLdPdPCORgeE3ZUb9izHRrgu75i4rIJEUK9dre9j1QeCFRVcbCTlluZXGHgGjrs68qcLniJmBYyTrxEtpYWcvSIjOO4ZJ8Cl0962z11Dc1; DudleyMBC_CookieConsent=%7B%22siteimprove%22%3Afalse%2C%22googleanalytics%22%3Afalse%2C%22sitecode%22%3Atrue%2C%22googlerecaptcha%22%3Atrue%7D; TS015c65a0=0104e7c0628a6b3839695e6ea86d0454d2d2e84a56d6e93d5cc11000c33d0f0115f72f8a44477b1ec58001d9fea9156118c8839074; TS1f705e18027=08456f7273ab2000e41ca70e3c02ec27cf377b960eafcb20d75624ba45293241de845c3f13d91b5d082f62bcc51130005975b703cc3613546a4681f7f563e7525758bb8af43267c7e81093a02b4facbc0e81f6f65856fda5ed75a7f190695f6e; TS00000000076=08456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1080f108c5d09d00080a7be6745ce77500036d593bdb3ef692fd84d2747fcc4a1ccc568201ff4401d5e34f83ad7b6747c730f97ccfb4cf5978471e0bf0c3cc4fecd2d6a7617c07a40d9a16b368660f5b11e6f26c374e301ac86aee497217bd4e79778266cfb32e78a5163212fafaba2565bd5918e510cae36e7c3f68aa870c5197fefd73cfe4be76c1bcf7418965d6e555d78f2b260922221d31fadbacc9fec171f89e9185296a564b0a2552f3a42ac0ced86f3078c3b67eb0e4db826649e172ea03fcfe6fdd98585f8e371b1331afaf982e595387b115461; TSPD_101_DID=08456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1080f108c5d0638003c0368f1940fca065c701bd2bdaea6706586d687d70f71cf5c6e311160062a26824c400d5b847520a42f1dcdd4b5cf0b95b05e6606279f3d",'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            r = requests.get(link, timeout=15,verify=True)
            soup=None
            if r.headers['content-type']=="application/json":
                a=json.loads(r.text)
                soup = BeautifulSoup(a["html"], 'html.parser')
            else:
                soup = BeautifulSoup(r.text, 'html.parser')
            
            # print(soup)
            lista=soup.select(listas)
            # print(lista[0].prettify())
            
            # print(len(lista))
            if len(lista) == 0:
                break
            for a in lista:
                # print(a)
                s=None
                if datesss:
                    s=a.select_one(datesss).getText().replace(replaceDate,"") if replaceDate else a.select_one(datesss).getText()
                if replaceRegex:
                    cop=re.search(replaceRegex, a.select_one(datesss).getText())
                    s=cop.group() if cop else ""
                if getDatea:
                    s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
                # print(s)
                # print(a.select_one("a").get("href"))
                imajin=linkedin2+a.select_one(imajinasi).get("src") if a.select_one(imajinasi) else "" if imajinasi else ""
                titulos=a.select_one("a").get("title") if a.select_one("a") else ""
                
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a.select_one(title).getText().replace('\n', ' ').replace('\r', '').strip() if a.select_one(title) else titulos if titulos else ""
                        )
                    coki=getBody(linkedin+a.select_one(href).get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina)
                    papa.body=coki[0] if len(coki) > 0 and coki else ""
                    papa.image=linkedin2+coki[1] if len(coki) > 0 and coki[1] != "" else imajin
                    papa.save()
                    
                else:
                    setop=True
                    # break
            if setop:
                break
            number+=1
    except Exception as e:
        print("err "+numero+" ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = parse(dates.strip(),dayfirst=True)
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = parse(dates.strip(),dayfirst=True)
    dateCompare = date(2020, 6, 1)  
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared

def getBody(link,content="sam",imajin="sam",linkedin2=""):
    panda1=""
    image=""
    try:
        headers={"Cookie":"TSd9457995075=0402b10008456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1:080f108c5d03200016030882bf3cd6354ab0f1cd11b648211a8099ed8e77e5c4d496f90782b6eb55a00108456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1080f108c5d1098005c466fe9b634dd8c47908baa492b8ffcca6c8f68847f0266ab89ff761209f0944614d490bb192a96207c4218bfcae5ee62d6e8b09a5e01f483e0c11fc435ebd8703f135d9daad70c936849e34569e5ebba5f90dbf6006689ac788a722d285bff4272c33511e1824878e2dc098d76c83abfb470cf4d3ad84d027380cd4de1533eba725f76e4985c5e9e055a9933484853c7f1e444eee287230001000b00008456f7273ab20003312cf6cfbaf7d26fe1dac52d19f0f91a43e45297ccbfc617990e3b3e7f77f7408f88743f00a2800a6a890eb0f9f5bacce875f9e9082faf80bbf66e1be01641bac8f8eab4d69f7e0b682f1e9e553461401000; ASP.NET_SessionId=kojgbtfbklkwg2m3cc31akqp; __RequestVerificationToken=2ZbLdPdPCORgeE3ZUb9izHRrgu75i4rIJEUK9dre9j1QeCFRVcbCTlluZXGHgGjrs68qcLniJmBYyTrxEtpYWcvSIjOO4ZJ8Cl0962z11Dc1; DudleyMBC_CookieConsent=%7B%22siteimprove%22%3Afalse%2C%22googleanalytics%22%3Afalse%2C%22sitecode%22%3Atrue%2C%22googlerecaptcha%22%3Atrue%7D; TS015c65a0=0104e7c0628a6b3839695e6ea86d0454d2d2e84a56d6e93d5cc11000c33d0f0115f72f8a44477b1ec58001d9fea9156118c8839074; TS1f705e18027=08456f7273ab2000e41ca70e3c02ec27cf377b960eafcb20d75624ba45293241de845c3f13d91b5d082f62bcc51130005975b703cc3613546a4681f7f563e7525758bb8af43267c7e81093a02b4facbc0e81f6f65856fda5ed75a7f190695f6e; TS00000000076=08456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1080f108c5d09d00080a7be6745ce77500036d593bdb3ef692fd84d2747fcc4a1ccc568201ff4401d5e34f83ad7b6747c730f97ccfb4cf5978471e0bf0c3cc4fecd2d6a7617c07a40d9a16b368660f5b11e6f26c374e301ac86aee497217bd4e79778266cfb32e78a5163212fafaba2565bd5918e510cae36e7c3f68aa870c5197fefd73cfe4be76c1bcf7418965d6e555d78f2b260922221d31fadbacc9fec171f89e9185296a564b0a2552f3a42ac0ced86f3078c3b67eb0e4db826649e172ea03fcfe6fdd98585f8e371b1331afaf982e595387b115461; TSPD_101_DID=08456f7273ab28003780f7115e1cd5a548c11f3482d749b01fe8784ed8a7ec94cd098135fa6bd37cfda202a0b8584aa1080f108c5d0638003c0368f1940fca065c701bd2bdaea6706586d687d70f71cf5c6e311160062a26824c400d5b847520a42f1dcdd4b5cf0b95b05e6606279f3d",'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        
        r = requests.get(link.strip(), timeout=15,verify=True)
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup)
        
        panda=soup.select(content) if soup.select(content) else []
        # print(panda)
        
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        image=soup.select(imajin) if soup.select(imajin) else []
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
