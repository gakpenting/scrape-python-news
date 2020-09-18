
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link338():
    getList(
    numero="338",
        LA_name="East Suffolk",
        LA_pr="https://www.eastsuffolk.gov.uk/news/",
    links="https://www.eastsuffolk.gov.uk/news/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".blogEntry > *:not(.authorDate)",
    imajina="#mainImage > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.eastsuffolk.gov.uk")
