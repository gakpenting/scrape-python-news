from peewee import *


# Connect to a MySQL database on network.
mysql_db = MySQLDatabase('all_link', user='root', password='helloworld',
                         host='127.0.0.1', port=6603 ,charset='utf8mb4')

class Links(Model):

    id = PrimaryKeyField(null=False)
    main_link=TextField(null=True)
    link=TextField(null=True)
    source=TextField(null=True)
    title=TextField(null=True)
    date=DateTimeField(null=True)
    body=TextField(null=True)
    image=TextField(null=True)
    
    class Meta:
        database = mysql_db
        db_table = "links"

Links.create_table(Links)