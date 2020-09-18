
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link199():
    getList(
     numero="199",
    LA_name="City of Edinburgh",
    LA_pr="https://www.edinburgh.gov.uk/news",
    links="https://www.edinburgh.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".summary, .editor",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")




