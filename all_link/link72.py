
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link72():
    getList(
    numero="72",
    LA_name="Gloucester",
    LA_pr="https://www.gloucestershire.gov.uk/gloucestershire-county-council-news/",
    links="https://www.gloucestershire.gov.uk/gloucestershire-county-council-news/rss/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#maincontent > div > div.pcg-news-page > div > div.col-sm-8.col-md-9 > div > div.pcg-rte-wrapper",
    imajina="#maincontent > div > div.pcg-news-page > div > div.col-sm-8.col-md-9 > div > div.pcg-news-info.row > div.pcg-news-img-block.col-md-6 > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.gloucestershire.gov.uk")
