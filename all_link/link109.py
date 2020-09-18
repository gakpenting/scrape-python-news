
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link109():
    getList(
    numero="109",
    LA_name="Oxford",
    LA_pr="https://www.oxford.gov.uk/news",
    links="https://www.oxford.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".site-content > article *:not(li):not(ul):not(a):not(strong):not(small)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

