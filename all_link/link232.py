
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getBody,getDate as getDatea


def link232():
    getList(
         content="div[itemprop='articleBody']",
        imajina="sam",
numero="232",
        LA_name="Erewash",
        LA_pr="https://www.erewash.gov.uk/index.php/news-and-events/latest-news-mnu.html",
    links="https://www.erewash.gov.uk/index.php/news-and-events/latest-news-mnu.feed?type=rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2=""
    )
