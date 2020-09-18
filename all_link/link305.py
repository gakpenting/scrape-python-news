
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link305():
    getList(
        datea=None,
        getDatea=None,
numero="305",
        LA_name="Ashfield",
        LA_pr="https://www.ashfield.gov.uk/mediacentre/news-and-updates/",
    links="https://www.ashfield.gov.uk/mediacentre/news-and-updates/",
    listas=".listing-item",
    datesss=".listing-date",
    replaceDate=None,
    title="h3",
    getBody=getBody,
    content="#bodyContent > div.grid-content > div > div > div > div > p",
    imajina=".listing-item-title > img",
    linkedin="https://www.ashfield.gov.uk",
    href="a",
    linkedin2="https://www.ashfield.gov.uk")





