
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link128():
    getList(
    numero="128",
    LA_name="Rugby",
    LA_pr="https://www.rugby.gov.uk/news",
    links="https://www.rugby.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > *:not(.page-comments) >article>*>*:not(img):not(figCaption):not(li)",
    imajina="#content > *:not(.page-comments) >article>*>img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

