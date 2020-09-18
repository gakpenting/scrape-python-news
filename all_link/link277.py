
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate as getDatea,getBody
def link277():
    getList(
           numero="277",
        LA_name="Rossendale",
        LA_pr="http://www.rossendalenews.org.uk/",
    links="https://www.rossendalenews.org.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".the_content > p",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

