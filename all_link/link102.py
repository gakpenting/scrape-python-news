
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link102():
    getList(
    numero="102",#gausah diisi
    LA_name="Kettering",#gausah diisi
    LA_pr="https://www.kettering.gov.uk/news",#gausah diisi
    links="https://www.kettering.gov.uk/rss/news",
    listas="item",#gausah diisi
    datesss="pubDate",#kadang kudu diisi
    replaceDate=None,#gausah diisi
    titles="title",#gausah diisi
    getBody=getBody,#gausah diisi
    content="#content > *:not(.page-heading):not(.list):not(.grid)",
    imajina="sam",
    imajinasi="sam",#gausah diisi
    linkedin="",#kadang kudu diisi
    href="link",#gausah diisi
    linkedin2=""#kadang kudu diisi
    )
    #103-203

