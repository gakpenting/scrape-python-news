
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link418():
    getList(
    numero="418",
    LA_name="Tewkesbury",
    LA_pr="tewkesbury.gov.uk/news",
    links="https://www.tewkesbury.gov.uk/news?format=rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".sqs-block-content",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

