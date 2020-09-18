
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link331():
    getList(
        datea="time",
        getDatea=getDate,
numero="331",
        LA_name="Barnsley",
        LA_pr="https://www.barnsley.gov.uk/search?search=news",
    links="https://www.barnsley.gov.uk/news/",
    listas=".archive-list__item",
    datesss="div",
    replaceDate=None,
    title=".media__text",
    getBody=getBody,
    content="article > div > p",
    imajina=".gallery__active__link > img",
    linkedin="https://www.barnsley.gov.uk",
    href="a",
    linkedin2="https://www.barnsley.gov.uk")
