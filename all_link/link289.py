
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link289():
    getList(
    numero="289",
        LA_name="Broadland",
        LA_pr="https://www.broadland.gov.uk/news/archive",
    links="https://www.harrogate.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".editor , .lead",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

