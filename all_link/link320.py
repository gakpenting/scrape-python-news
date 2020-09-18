
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link320():
    getList(
    numero="320",
        LA_name="Midlothian",
        LA_pr="https://www.midlothian.gov.uk/news/archive",
    links="https://www.midlothian.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#main-content > article > div.column.offset-1.span-8.content.push-3.editor > div.editor",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")


