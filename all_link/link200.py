
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link200():
    getList(
       numero="200",
    LA_name="Moray",
    LA_pr="https://newsroom.moray.gov.uk/news",
    links="https://newsroom.moray.gov.uk/feed/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content-summary",
    imajina="div.hero-image.margin-xlarge-bottom > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

