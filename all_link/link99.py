
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link99():
    getList(
    numero="99",
    LA_name="Hambleton",
    LA_pr="https://www.hambleton.gov.uk/news",
    links="https://www.hambleton.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="article > *:not(.date):not(h2):not(ul)",
    imajina="article > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

