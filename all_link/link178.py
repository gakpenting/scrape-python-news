
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link178():
    getList(
numero="178",
    LA_name="Boston",
    LA_pr="https://www.mybostonuk.com/news/",
    links="https://www.mybostonuk.com/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".entry-content",
    imajina=".entry-content > p > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

