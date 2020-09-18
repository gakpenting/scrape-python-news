
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link136():
    getList(
    numero="136",
    LA_name="Swindon",
    LA_pr="https://www.swindon.gov.uk/news",
    links="https://www.swindon.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > .site-content__main> .editor>*",
    imajina="#content > .site-content__main> img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

