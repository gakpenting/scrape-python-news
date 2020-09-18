
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link253():
    getList(
    numero="253",
        LA_name="Manchester",
        LA_pr="https://www.manchester.gov.uk/news/",
    links="http://secure.manchester.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".news-article",
    imajina=".news-article > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="http:")
