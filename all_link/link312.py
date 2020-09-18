
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link312():
    getList(
    numero="312",
        LA_name="Aberdeen City",
        LA_pr="https://news.aberdeencity.gov.uk/",
    links="https://news.aberdeencity.gov.uk/feed/en",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".text_companyprofile",
    imajina="sam",
    imajinasi="image",
    linkedin="",
    href="link",
    linkedin2="")



