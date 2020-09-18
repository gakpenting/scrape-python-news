
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link195():
    getList(
    numero="195",
    LA_name="Mansfield",
    LA_pr="https://www.mansfield.gov.uk/news",
    links="https://www.mansfield.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".page-content > *:not(.date):not(ul)",
    imajina=".page-content > figure > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.mansfield.gov.uk")

