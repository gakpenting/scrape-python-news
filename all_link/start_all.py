from all_link.link1 import link1 
from all_link.link2 import link2
from all_link.link3 import link3
from all_link.link4 import link4
from all_link.link5 import link5
from all_link.link6 import link6
from all_link.link7 import link7
from all_link.link8 import link8
from all_link.link9 import link9
from all_link.link10 import link10
from all_link.link11 import link11
from all_link.link12 import link12
from all_link.link13 import link13
from all_link.link14 import link14
from mysqls.pandasql import StartScrape
def start_all():
    from datetime import datetime
    print("scraping started")
    poldi,created=StartScrape.get_or_create(id=1)
    poldi.date=datetime.now()
    poldi.save()
    link1()
    link2()
    link3()
    link4()
    link5()
    link6()
    link7()
    link8()
    link9()
    link10()
    link11()
    link12()
    link13()
    link14()