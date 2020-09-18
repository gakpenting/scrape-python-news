import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from dateutil.parser import parse
from mysqls.pandasql import Links
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link10():
    getList(
    numero="10",
    LA_name="Ealing",
    LA_pr="https://ealingnewsextra.co.uk/category/latest-news/",
    links="http://ealingnewsextra.co.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".single-post-content",
    imajina="figure > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

