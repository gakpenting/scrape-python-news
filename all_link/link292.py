
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link292():
    getList(
        datea=None,
        getDatea=None,
        dayfirst=True,
numero="292",
        LA_name="Craven",
        LA_pr="https://www.cravendc.gov.uk/news/",
    links="https://www.cravendc.gov.uk/news/latest-news/",
    listas=".latest-news-inner",
    datesss="p",
    replaceDate="Published: ",
    title="h2",
    getBody=getBody,
    content=".container > div > p",
    imajina=".news-image > img",
    linkedin="https://www.cravendc.gov.uk",
    href="a",
    linkedin2="https://www.cravendc.gov.uk")


