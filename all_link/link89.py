
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link89():
    getList(
    numero="89",
    LA_name="Wyre",
    LA_pr="https://www.wyre.gov.uk/news/",
    links="https://www.wyre.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".news-article > *:not(h1):not(small)",
    imajina=".news-article > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

