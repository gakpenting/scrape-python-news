import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link221():
    getList(
  numero="221",
    LA_name="Reading",
    LA_pr="http://news.reading.gov.uk/pr/",
    links="http://news.reading.gov.uk/feed/",
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

