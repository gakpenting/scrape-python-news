
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link126():
    getList(
    numero="126",
    LA_name="Wales",
    LA_pr="https://gov.wales/announcements",
    links="https://gov.wales/announcements/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".paragraph>div>*",
    imajina=".page__image>div>img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://gov.wales")

