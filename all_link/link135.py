
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link135():
    getList(
    numero="135",
    LA_name="Calderdale",
    LA_pr="https://news.calderdale.gov.uk/author/calderdale-council/",
    links="https://news.calderdale.gov.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".entry-content >*:not(div)",
    imajina=".entry-content > div > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

