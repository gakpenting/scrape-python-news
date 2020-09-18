
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link282():
    getList(
    numero="282",
        LA_name="Oadby and Wigston",
        LA_pr="https://www.oadby-wigston.gov.uk/pages/news",
    links="https://www.oadby-wigston.gov.uk/feeds/news",
    listas="entry",
    datesss="published",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".body > p",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

