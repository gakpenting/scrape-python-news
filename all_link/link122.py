
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link122():
    getList(
    numero="122",
    LA_name="Reigate and Banstead",
    LA_pr="http://www.reigate-banstead.gov.uk/news",
    links="https://www.reigate-banstead.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > *:not(:first-child):not(#feedback):not(:last-child)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

