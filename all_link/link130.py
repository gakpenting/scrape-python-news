
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link130():
    getList(
    numero="130",
    LA_name="Birmingham",
    LA_pr="https://www.birmingham.gov.uk/news",
    links="https://www.birmingham.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > .editor>*",
    imajina="#content > *>img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

