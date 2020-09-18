from peewee import *
from datetime import datetime

# Connect to a MySQL database on network.

# mysql_db = MySQLDatabase('all_link', user='root', password='helloworld',
#                          host='127.0.0.1', port=6603 ,charset='utf8mb4')
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
def deleteWhere(LA_name=None,LA_pr=None):
    q = Links.delete().where(Links.LA_name == LA_name,Links.LA_pr == LA_pr)
    q.execute()
def deleteAll():
    q = Links.delete()
    q.execute()
Links.create_table(Links)
StartScrape.create_table(StartScrape)
