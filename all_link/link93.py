
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link93():
    getList(
    numero="93",
    LA_name="Melton",
    LA_pr="http://www.melton.gov.uk/ournews",
    links="http://www.melton.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content > *:not(h1):not(small):not(ul):not(nav)",
    imajina=".content > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

