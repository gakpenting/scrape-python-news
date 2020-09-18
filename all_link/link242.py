
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getBody,getDate as getDatea
def link242():
    getList(
        content=".content-body , .content-summary",
        imajina=".hero-image > img",
    numero="242",
        LA_name="Forest of Dean",
        LA_pr="https://www.fdean.gov.uk/residents/latest-news-events/",
    links="https://news.fdean.gov.uk/feed/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
