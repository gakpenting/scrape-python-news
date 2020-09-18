
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link325():
    getList(
        datea=None,
        getDatea=None,
numero="325",
        LA_name="West Lothian",
        LA_pr="https://news.westlothian.gov.uk/",
    links="https://news.westlothian.gov.uk/",
    listas="article.feed__item",
    datesss="date",
    replaceDate=None,
    title="h1",
    getBody=getBody,
    content=".article__body > div > div > p",
    imajina=".article__body > div > div > img",
    linkedin="http://www.southkesteven.gov.uk/",
    href="a",
    linkedin2="http://www.southkesteven.gov.uk/")


