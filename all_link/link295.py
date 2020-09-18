
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
import html
def link295():
    getList(
        datea=None,
        content="sam",
        imajina="",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="295",
        LA_name="Redcar and Cleveland",
        LA_pr="https://www.redcar-cleveland.gov.uk/News/Pages/news.aspx",
        links=None,
        listas=None,
        datesss=None,
        replaceDate=None,
        title=None,
        getBody=None,
        imajinasi=None,
        linkedin="",
        href="a",
        linkedin2="https://www.redcar-cleveland.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="295",LA_name="Redcar and Cleveland",LA_pr="https://www.redcar-cleveland.gov.uk/News/Pages/news.aspx",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        pageId=None
        while True:
            namber=str(number)
            setop=False
            link="https://www.redcar-cleveland.gov.uk//news/_vti_bin/client.svc/ProcessQuery"
            headers={"X-RequestDigest":"0x8A9856F1726B4CD7E029A6CB07DBB61843AF62FB39048B80D0F5D21F14115D641ED1DE1C6F2EEF5F1723825D5D6CF88F56A0194C8F51134987EB0B97BD0A7B2C,04 Sep 2020 11:46:03 -0000",'Content-Type': 'application/xml','User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            dateaa=str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day)
            burofax='<Property Name="ListItemCollectionPosition" TypeId="{922354eb-c56a-4d88-ad59-67496854efe1}"><Property Name="PagingInfo" Type="String">%s</Property></Property>' % (html.escape(pageId) if pageId else "")
            papap=burofax if pageId else '<Property Name="ListItemCollectionPosition" Type="Null"></Property>'
            data="""
<Request xmlns="http://schemas.microsoft.com/sharepoint/clientquery/2009" SchemaVersion="15.0.0.0" LibraryVersion="16.0.0.0" ApplicationName="Javascript Library"><Actions><ObjectPath Id="1" ObjectPathId="0" /><ObjectPath Id="3" ObjectPathId="2" /><ObjectPath Id="5" ObjectPathId="4" /><ObjectPath Id="7" ObjectPathId="6" /><ObjectIdentityQuery Id="8" ObjectPathId="6" /><ObjectPath Id="10" ObjectPathId="9" /><Query Id="11" ObjectPathId="9"><Query SelectAllProperties="true"><Properties /></Query><ChildItemQuery SelectAllProperties="true"><Properties /></ChildItemQuery></Query></Actions><ObjectPaths><StaticProperty Id="0" TypeId="{3747adcd-a3c3-41b9-bfab-4a64dd2f1e0a}" Name="Current" /><Property Id="2" ParentId="0" Name="Web" /><Property Id="4" ParentId="2" Name="Lists" /><Method Id="6" ParentId="4" Name="GetByTitle"><Parameters><Parameter Type="String">Pages</Parameter></Parameters></Method><Method Id="9" ParentId="6" Name="GetItems"><Parameters><Parameter TypeId="{3d248d7b-fc86-40a3-aa97-02a75d69fb8a}"><Property Name="AllowIncrementalResults" Type="Boolean">false</Property><Property Name="DatesInUtc" Type="Boolean">true</Property><Property Name="FolderServerRelativePath" Type="Null" /><Property Name="FolderServerRelativeUrl" Type="Null" />%s<Property Name="ViewXml" Type="String">&lt;View&gt;&lt;RowLimit&gt;5&lt;/RowLimit&gt;&lt;Query&gt;&lt;Where&gt;&lt;And&gt;&lt;And&gt;&lt;Geq&gt;&lt;FieldRef Name='Created' /&gt;&lt;Value Type='DateTime'&gt;2020-06-01&lt;/Value&gt;&lt;/Geq&gt;&lt;Leq&gt;&lt;FieldRef Name='Created' /&gt;&lt;Value IncludeTimeValue='TRUE' Type='DateTime'&gt;%s&lt;/Value&gt;&lt;/Leq&gt;&lt;/And&gt;&lt;Neq&gt;&lt;FieldRef Name='FileLeafRef' /&gt;&lt;Value Type='File'&gt;default.aspx&lt;/Value&gt;&lt;/Neq&gt;&lt;/And&gt;&lt;/Where&gt;&lt;OrderBy&gt;&lt;FieldRef Name='ID' Ascending='FALSE'/&gt;&lt;/OrderBy&gt;&lt;/Query&gt;&lt;/View&gt;</Property></Parameter></Parameters></Method></ObjectPaths></Request>
            """ % (papap,dateaa)
            r = requests.post(link, timeout=15,verify=False,data=data,headers=headers)
            soup=None
            
            b=json.loads(r.text)
                
            
            # print(soup)
            if b[14]["ListItemCollectionPosition"]:
                pageId=b[14]["ListItemCollectionPosition"]["PagingInfo"]
            else:
                break
            lista=b[14]["_Child_Items_"]
            # print(lista[0].prettify())
            
            if len(lista) == 0:
                break
            for a in lista:
                
                s=a["Created_x0020_Date"]
                
                # print(s)
                # print(a.select_one("a").get("href"))
                
                
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a["Title"]
                        )
                    papa.body=BeautifulSoup(a["PublishingPageContent"],"html.parser").text if a["PublishingPageContent"] else ""
                    papa.image=linkedin2+BeautifulSoup(a["PublishingRollupImage"],"html.parser").select_one("img").get("src") if a["PublishingRollupImage"] else ""
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


