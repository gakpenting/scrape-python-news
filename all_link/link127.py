
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link127():
    getList(
    numero="127",
    LA_name="Warwickshire",
    LA_pr="https://news.warwickshire.gov.uk/",
    links="https://www.warwickshire.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content>.page-content>*:not(.rss-feed):not(page-meta)>*:not(.meta):not(.imageCaption):not(img)",
    imajina="#content>.page-content>*:not(.rss-feed):not(page-meta)>*>img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.warwickshire.gov.uk")

