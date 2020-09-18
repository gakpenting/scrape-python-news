
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link120():
    getList(
    numero="120",
    LA_name="Babergh",
    LA_pr="https://www.babergh.gov.uk/news/",
    links="https://www.babergh.gov.uk/news/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".blogEntry > *:not(:first-child)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

