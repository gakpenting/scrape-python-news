
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getBody,getDate as getDatea
def link243():
    getList(
        content=".td-post-content",
        imajina=".td-modal-image > img",
    numero="243",
        LA_name="South Gloucestershire",
        LA_pr="https://sites.southglos.gov.uk/newsroom/",
    links="https://sites.southglos.gov.uk/newsroom/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

