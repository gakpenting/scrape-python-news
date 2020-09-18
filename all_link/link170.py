
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link170():
    getList(
    pagis=1,
    numero="170",
    LA_name="Thanet",
    LA_pr="https://www.thanet.gov.uk/latest-news/",
    links="https://www.thanet.gov.uk/latest-news/page/",
    listas=".news.home",
    datesss=".field.field-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".field.field-title",
    getBody=getBody,
    content=".field.field-body > p",
    imajina="sam",
    imajinasi="img",
    linkedin="",
    href="a",
    linkedin2="")


