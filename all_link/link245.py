
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getBody,getDate as getDatea

def link245():
    getList(
        content=".text_companyprofile",
        imajina=".gallery_thumbnail_single > img",
        numero="245",
        LA_name="Hackney",
        LA_pr="https://news.hackney.gov.uk/",
    links="https://news.hackney.gov.uk/feed/en",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https:"
    )

