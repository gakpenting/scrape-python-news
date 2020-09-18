
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link276():
    getList(
    numero="276",
        LA_name="Ribble Valley",
        LA_pr="https://www.ribblevalley.gov.uk/news",
    links="https://www.ribblevalley.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".editor",
    imajina="figure > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https:")
