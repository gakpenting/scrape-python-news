
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link369():
    getList(
        datea=None,
        getDatea=None,
numero="369",
        LA_name="Arun",
        LA_pr="https://www.arun.gov.uk/news-archive/",
    links="https://www.arun.gov.uk/news-archive/",
    listas="article.post-inner",
    datesss="time",
    replaceDate=None,
    title="h3",
    getBody=getBody,
    content="div.text",
    imajina="#placement-7-1 > div > div > div > div.content-wrapper-inner > article > div > p > img",
    linkedin="https://www.arun.gov.uk",
    href="a",
    linkedin2="https://www.arun.gov.uk")

