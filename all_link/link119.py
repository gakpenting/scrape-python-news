
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link119():
    getList(
    numero="119",
    LA_name="Tamworth",
    LA_pr="https://www.tamworth.gov.uk/news",
    links="https://www.tamworth.gov.uk/news/rss.xml",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".field-items > * > *",
    imajina=".field-items > * img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.tamworth.gov.uk")

