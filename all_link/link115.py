
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link115():
    getList(
    numero="115",
    LA_name="Sedgemoor",
    LA_pr="https://www.sedgemoor.gov.uk/article/717/Latest-News-Announcements",
    links="https://www.sedgemoor.gov.uk/rss",
    listas="item",
    datesss="updated",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#main > *:not(:nth-child(1)):not(:nth-child(2))",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

