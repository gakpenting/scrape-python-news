
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link364():
    getList(
    numero="364",
        LA_name="Nuneaton and Bedworth",
        LA_pr="https://www.nuneatonandbedworth.gov.uk/news",
    links="https://www.nuneatonandbedworth.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".summary, .editor",
    imajina="#content > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https:")
