
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link300():
    getList(
    numero="300",
        LA_name="Armagh City, Banbridge and Craigavon",
        LA_pr="https://www.armaghbanbridgecraigavon.gov.uk/news/",
    links="https://www.armaghbanbridgecraigavon.gov.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".td-post-content > p",
    imajina="figure > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

