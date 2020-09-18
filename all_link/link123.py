
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link123():
    getList(
    numero="123",
    LA_name="Spelthorne",
    LA_pr="https://www.spelthorne.gov.uk/article/16409/News",
    links="https://www.spelthorne.gov.uk/news?rss=true",
    listas="item",
    datesss="updated",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".a-body > *:not(:first-child)",
    imajina=".a-relimage >img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

