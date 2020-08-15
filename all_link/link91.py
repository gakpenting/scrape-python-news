
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link91():
    getList(
    numero="91",
    LA_name="Harborough",
    LA_pr="https://www.harborough.gov.uk/news",
    links="https://www.harborough.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="article > *:not(h1):not(.small)",
    imajina=".editor > p > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.harborough.gov.uk")

