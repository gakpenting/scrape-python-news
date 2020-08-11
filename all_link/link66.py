import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link66():
    getList(
    numero="66",
    LA_name="Southend-on-Sea",
    LA_pr="https://www.southend.gov.uk/newsroom/home",
    links="http://feeds.bbci.co.uk/news/england/essex/rss.xml",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".story-body__inner > *:not(figure)",
    imajina=".js-image-replace",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
