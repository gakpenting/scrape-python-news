
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getBody,getDate as getDatea

def link231():
    getList(
        content=".td-post-content",
        imajina=".td-post-featured-image > img",
        numero="231",
        LA_name="Derby",
        LA_pr="https://news.derby.gov.uk/",
    links="https://news.derby.gov.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2=""
    )
