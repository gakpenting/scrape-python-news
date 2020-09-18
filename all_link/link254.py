
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link254():
    getList(
            numero="254",
        LA_name="Stockport",
        LA_pr="https://www.stockport.gov.uk/news",
    links="https://www.stockport.gov.uk/news/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="article",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="http:")

