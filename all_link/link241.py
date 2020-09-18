
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getBody,getDate as getDatea
def link241():
    getList(
        content=".cell-contained > *:not(:nth-child(1)):not(:nth-child(2))",
        imajina=".hero-image > img",
    numero="241",
        LA_name="Cotswold",
        LA_pr="https://news.cotswold.gov.uk/",
    links="https://news.cotswold.gov.uk/feed/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
