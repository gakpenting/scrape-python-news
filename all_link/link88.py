
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link88():
    getList(
    numero="88",
    LA_name="Lancashire",
    LA_pr="https://www.lancashire.gov.uk/news/",
    links="http://www3.lancashire.gov.uk/corporate/news/press_releases/rss2feed.asp",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#pageContent > div > div:nth-child(1) > div > div > div.col-md-8 > p:not(:nth-child(2))",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

