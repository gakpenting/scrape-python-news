
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getBody,getDate as getDatea
from all_link.page.rss import getList
def link239():
    getList(
        content="div[itemprop='text']",
        imajina=".w-blogpost-preview > img",
    numero="239",
        LA_name="Epping Forest",
        LA_pr="https://www.eppingforestdc.gov.uk/category/news/",
    links="https://www.eppingforestdc.gov.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
