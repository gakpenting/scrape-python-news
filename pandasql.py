from peewee import *
from datetime import datetime

# Connect to a MySQL database on network.
# mysql_db = MySQLDatabase('all_link', user='admin', password='England123&',
#                          host='kedalert-1.cf8fsz14idww.eu-west-2.rds.amazonaws.com', port=3306 ,charset='utf8mb4')
mysql_db = MySQLDatabase('all_link', user='root', password='helloworld',
                         host='127.0.0.1', port=6603 ,charset='utf8mb4')
class Links(Model):

    id = PrimaryKeyField(null=False)
    LA_name=TextField(null=True)
    LA_pr=TextField(null=True)
    title=TextField(null=True)
    date=DateTimeField(null=True)
    body=TextField(null=True)
    image=TextField(null=True)
    
    class Meta:
        database = mysql_db
        db_table = "links"
class StartScrape(Model):
    id = PrimaryKeyField(null=False)
    date=date=DateTimeField(default=datetime.now)
    
    
    class Meta:
        database = mysql_db
        db_table = "start_scrape"
Links.create_table(Links)
StartScrape.create_table(StartScrape)