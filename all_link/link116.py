
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link116():
    getList(
    numero="116",
    LA_name="Doncaster",
    LA_pr="https://www.doncaster.gov.uk/news",
    links="https://www.doncaster.gov.uk/news/latestnews.xml",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="main > div * :not(:nth-child(0)):not(:nth-child(1)) :not(:last-child) :not(div):not(span):not(iframe)",
    imajina="#content > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

