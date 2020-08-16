
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link101():
    getList(
    numero="101",
    LA_name="Stockton-on-Tees",
    LA_pr="https://www.stockton.gov.uk/news/",
    links="https://www.stockton.gov.uk/rss",
    listas="item",
    datesss="pubdate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".media > *:not(.datesmall)",
    imajina=".media > div > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.stockton.gov.uk")

