
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link114():
    getList(
    numero="114",
    LA_name="Scottish Borders",
    LA_pr="https://www.scotborders.gov.uk/news",
    links="https://www.scotborders.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > article> div.editor > *",
    imajina="#content > article >img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

