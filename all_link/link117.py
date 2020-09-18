
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link117():
    getList(
    numero="117",
    LA_name="Stafford",
    LA_pr="https://www.staffordbc.gov.uk/news-articles",
    links="https://www.staffordbc.gov.uk/news-feed.rss",
    listas="item",
    getDatea=getDate,
    datea="#main-content > div:nth-child(2) > div:nth-child(1) > div.col-lg-8.col-md-8.col-sm-12 > div.region.region-content > article > div > div > div.col-md-12 > div:nth-child(1) > span > h4",
    datesss=None,
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#main-content > div:nth-child(2) > div:nth-child(1) > div.col-lg-8.col-md-8.col-sm-12 > div.region.region-content > article > div > div > div.col-md-12 > div:nth-child(3) > div > p",
    imajina="#main-content > div:nth-child(2) > div:nth-child(1) > div.col-lg-8.col-md-8.col-sm-12 > div.region.region-content > article > div > div > div.col-md-12 > div:nth-child(1) > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.staffordbc.gov.uk",
    dayfirst=True)

