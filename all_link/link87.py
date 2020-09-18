
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link87():
    getList(
    numero="87",
    LA_name="Tunbridge Wells",
    LA_pr="http://www.tunbridgewells.gov.uk/residents/news",
    links="http://www.tunbridgewells.gov.uk/residents/news/rss-feeds/news-rss-feed",
    listas="item",
    datesss=None,
    replaceDate=None,
    titles="title",
    getDatea=getDate,
    datea="p.date",
    getBody=getBody,
    content="#main_content > div > *:not(h1):not(.date)",
    imajina="#main_content img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

