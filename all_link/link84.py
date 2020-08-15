
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link84():
    getList(
    numero="84",
    LA_name="Watford",
    LA_pr="https://www.watford.gov.uk/news",
    links="https://www.watford.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".editor",
    imajina="#content > article > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

