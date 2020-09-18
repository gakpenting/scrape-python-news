
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link287():
    getList(
    numero="287",
        LA_name="Liverpool",
        LA_pr="https://liverpoolexpress.co.uk/",
    links="https://liverpoolexpress.co.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".entry-content",
    imajina=".flipboard-image",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

