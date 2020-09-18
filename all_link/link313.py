
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link313():
    getList(
    numero="313",
        LA_name="Aberdeenshire",
        LA_pr="https://www.aberdeenshire.gov.uk/news/",
    links="https://online.aberdeenshire.gov.uk/apps/news/rss.aspx",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#mainContent > p",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

