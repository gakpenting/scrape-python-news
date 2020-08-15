
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link79():
    getList(
    numero="79",
    LA_name="Salford",
    LA_pr="https://www.salford.gov.uk/your-council/news/",
    links="https://www.salford.gov.uk/news/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#news-page > div:nth-child(1) > div.col-xs-12.col-md-8",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

