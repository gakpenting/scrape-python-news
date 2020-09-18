
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link317():
    getList(
        datea=None,
        getDatea=None,
numero="317",
        LA_name="Falkirk",
        LA_pr="https://www.falkirk.gov.uk/news/",
    links="https://www.falkirk.gov.uk/news/",
    listas="li[itemtype='http://schema.org/NewsArticle']",
    datesss="time",
    replaceDate=None,
    title="a > span",
    getBody=getBody,
    content="div[itemprop='articleBody']",
    imajina="div[itemprop='articleBody'] > img",
    linkedin="https://www.falkirk.gov.uk",
    href="a",
    linkedin2="https://www.falkirk.gov.uk")
