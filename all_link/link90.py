
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link90():
    getList(
    numero="90",
    LA_name="Blaby",
    LA_pr="https://www.blaby.gov.uk/your-council/news-and-awards/news/",
    links="https://www.blaby.gov.uk/news.rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".right > *:not(h2):not(h1):not(.last-update):not(.additional-content)",
    imajina=".articleImage",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.blaby.gov.uk")

