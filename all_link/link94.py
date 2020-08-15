
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link94():
    getList(
    numero="94",
    LA_name="Sefton",
    LA_pr="http://mysefton.co.uk/category/latest-news/",
    links="https://mysefton.co.uk/category/latest-news/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="section.entry-content",
    imajina="section.entry-content > a > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

