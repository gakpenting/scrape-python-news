
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link85():
    getList(
    numero="85",
    LA_name="Kent",
    LA_pr="https://kccmediahub.net/",
    links="https://kccmediahub.net/feed",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="span.entry-content",
    imajina="span.entry-content > div > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

