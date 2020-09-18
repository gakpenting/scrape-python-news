
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link309():
    getList(
    numero="309",
        LA_name="Oxfordshire",
        LA_pr="https://news.oxfordshire.gov.uk/",
    links="https://news.oxfordshire.gov.uk/feed/en",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".ppmodule_textblock, .text_companyprofile",
    imajina=".gallery_thumbnail_single > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https:")

