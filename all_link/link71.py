
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link71():
    getList(
    numero="71",
    LA_name="Eden",
    LA_pr="https://www.eden.gov.uk/your-council/news/",
    links="https://www.eden.gov.uk/rss/media-releases-rss/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content-page-holder > p",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

