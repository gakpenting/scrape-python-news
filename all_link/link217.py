
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link217():
    getList(
    numero="217",
    LA_name="Wrexham",
    LA_pr="https://news.wrexham.gov.uk/",
    links="https://news.wrexham.gov.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".page-content > *:not(.date):not(ul)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

