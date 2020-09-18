
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link303():
    getList(
    numero="303",
        LA_name="Mid and East Antrim",
        LA_pr="https://www.mynewsdesk.com/uk/meabc",
    links="https://www.mynewsdesk.com/uk/rss/current_news/97013",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".panel__text",
    imajina=".panel__media > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

