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
from all_link.link15 import link15
from all_link.link16 import link16
from all_link.link17 import link17
from all_link.link18 import link18
from all_link.link19 import link19
from all_link.link20 import link20
from all_link.link21 import link21
from all_link.link22 import link22
from all_link.link23 import link23
from all_link.link24 import link24
from all_link.link25 import link25
from all_link.link26 import link26
from all_link.link27 import link27
from all_link.link28 import link28
from all_link.link29 import link29
from all_link.link30 import link30
from all_link.link31 import link31
from all_link.link32 import link32
from all_link.link33 import link33
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
    link15()
    link16()
    link17()
    link18()
    link19()
    link20()
    link21()
    link22()
    link23()
    link24()
    link25()
    link26()
    link27()
    link28()
    link29()
    link30()
    link31()
    link32()
    link33()