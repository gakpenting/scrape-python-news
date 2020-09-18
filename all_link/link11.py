import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link11():
    getList(
    numero="11",
    LA_name="West Oxfordshire",
    LA_pr="westoxon.gov.uk/news",
    links="https://news.westoxon.gov.uk/feed/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content-summary, .content-body",
    imajina="body > main > div > div.c-width-large-3-4 > div.cell.cell-contained.cell-padding-large.release > div.hero-image.margin-xlarge-bottom > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
