
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link113():
    getList(
    numero="113",
    LA_name="Inverclyde",
    LA_pr="https://www.inverclyde.gov.uk/news",
    links="https://www.inverclyde.gov.uk/rss/news/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content >  *:not(:nth-child(1)):not(:nth-child(2)):not(:last-child):not(div):not(figure)",
    imajina=".content >  figure >img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.inverclyde.gov.uk")

