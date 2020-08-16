
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link95():
    getList(
    numero="95",
    LA_name="Breckland",
    LA_pr="https://www.breckland.gov.uk/latestnews",
    links="https://www.breckland.gov.uk/latestnews?rss=True",
    listas="item",
    datesss="updated",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="div.a-body",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

