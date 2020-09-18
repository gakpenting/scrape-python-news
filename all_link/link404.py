
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link404():
    getList(
    numero="404",
    LA_name="Mid Suffolk",
    LA_pr="midsuffolk.gov.uk/news",
    links="https://www.midsuffolk.gov.uk/news/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".blogEntry > p:not(.authorDate)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

