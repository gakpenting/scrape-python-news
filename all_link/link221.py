import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link221():
    getList(
    numero="221",
    LA_name="Reading",
    LA_pr="http://news.reading.gov.uk/pr/",
    links="http://news.reading.gov.uk/pr/",
    listas=".widget > ul:not(.wpp-list) > li",
    datesss="span.post-date",
    replaceDate=None,
    title="a",
    getBody=getBody,
    content="",
    imajina="",
    linkedin="",
    href="a",
    linkedin2="")

