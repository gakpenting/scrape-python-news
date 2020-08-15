
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link75():
    getList(
    numero="75",
    LA_name="Kingston upon Thames",
    LA_pr="https://www.kingston.gov.uk/news",
    links="https://www.kingston.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > div.container > div.site-content > article > *:not(time):not(h2)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

