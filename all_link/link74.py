
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link74():
    getList(
    numero="74",
    LA_name="Hounslow",
    LA_pr="https://www.hounslow.gov.uk/news",
    links="https://www.hounslow.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".editor",
    imajina="#content > div.editor > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

