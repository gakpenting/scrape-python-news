
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link98():
    getList(
    numero="98",
    LA_name="North Yorkshire",
    LA_pr="https://www.northyorks.gov.uk/news",
    links="https://www.northyorks.gov.uk/rss.xml",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content",
    imajina=".content img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.northyorks.gov.uk/")

