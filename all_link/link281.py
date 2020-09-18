
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link281():
    getList(
    numero="281",
        LA_name="North West Leicestershire",
        LA_pr="https://www.nwleics.gov.uk/pages/news",
    links="https://www.nwleics.gov.uk/feeds/news",
    listas="entry",
    datesss="published",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".body > p:not(:first-child)",
    imajina=".body > p > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")


