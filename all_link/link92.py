
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link92():
    getList(
    numero="92",
    LA_name="Hinckley and Bosworth",
    LA_pr="https://www.hinckley-bosworth.gov.uk/newsandpress",
    links="https://www.hinckley-bosworth.gov.uk/rss/press",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content.content--fullwidth > *:not(.small):not(.item-list)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

