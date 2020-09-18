
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link294():
    getList(
    numero="294",
        LA_name="York",
        LA_pr="https://www.york.gov.uk/homepage/47/news_centre",
    links="https://www.york.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".summary, .editor",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")


