import mysql.connector
import csv
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
# mydb = mysql.connector.connect(
#   host="kedalert-1.cf8fsz14idww.eu-west-2.rds.amazonaws.com",
#   user="admin",
#   password="England123&",
#   port=3306,
#   database="all_link"
# )
# mycursor = mydb.cursor()

# mycursor.execute("select LA_name,LA_pr from links group by LA_name")
# myresult = mycursor.fetchall()
# popo=[]
# nombre=0
# for x in myresult:
#     nombre+=1
#     # print(x)
#     popo.append({"LA_name":x[0],"LA_pr":x[1],"mamam":str(nombre)})
# print(myresult[0][1])
# create_csv(popo,"pancasila.csv")

ta=None
bu=None
copin=[]
with open('pancasila.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ta=list(csv_reader)
with open('DONE.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    bu=list(csv_reader)
cubby=ta[1:len(ta)]
camel=bu[1:len(bu)]
# print(camel[0])
cokidar=[]
nombre=0
for k in camel:
    if k[2]=="DONE":
        nombre+=1
        cokidar.append(k[0])
flopsi=[]
for l in cubby:
    flopsi.append(l[0])
polo=[]
cak=0
# print(len(cubby))
# print(len(cokidar))
for a in cokidar:
    if not a in flopsi:
        # print(a[0])
        cak+=1
        polo.append({"LA_name":a,"LA_pr":a,"mamam":str(cak)})
create_csv(polo,"NOTSCRAPED.csv")
poki=[]
# print(len(flopsi))
# p
for a in flopsi:
    if not a in cokidar:
        # print(a[0])
        cak+=1
        poki.append({"LA_name":a,"LA_pr":a,"mamam":str(cak)})
create_csv(poki,"NOTSCRAPED2.csv")
