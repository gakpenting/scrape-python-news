
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link96():
    getList(
    numero="96",
    LA_name="North Norfolk",
    LA_pr="https://www.north-norfolk.gov.uk/news/",
    links="https://www.north-norfolk.gov.uk/rss-news/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".rich-text > *:not(img):not(:nth-child(2))",
    imajina=".rich-text img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.north-norfolk.gov.uk")

