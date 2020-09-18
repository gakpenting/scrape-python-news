import csv
import requests
from bs4 import BeautifulSoup
ta=None
def create_csv(dict_data,name):
    csv_columns = ['LA_name','LA_pr','mamam']
    csv_file = name
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
with open('a.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ta=list(csv_reader)
print(ta[0])
csvList=[]
numba=0
for a in ta[1:len(ta)]:
    numba+=1
    print(numba)
    if a[2] != "DONE":
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        try:
            r = requests.get(a[1], timeout=15,verify=False,headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            mambo=""
            z=soup.select("a")
            j=soup.select("img")
            for k in z:
                if k:
                    mambo+=str(k.get("href"))+str(k.getText())+" "
            for l in j:
                if l:
                    mambo+=str(l.get("src"))+" "
            p=["Listing_List_GoToPage=2","page=2","/page/2","?p=2","lister"]
            if "rss" in mambo:
                csvList.append({"LA_name":a[0],"LA_pr":a[1],"mamam":"rss"})
            elif any(x in mambo for x in p):
                csvList.append({"LA_name":a[0],"LA_pr":a[1],"mamam":"page"})
            else:
                csvList.append({"LA_name":a[0],"LA_pr":a[1],"mamam":"golekono dewe"})
        except Exception as e:
            print(str(e))
        

create_csv(csvList,"panda.csv")

