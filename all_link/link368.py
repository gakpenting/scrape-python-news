
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link368():
    getList(
        datea=None,
        getDatea=None,
numero="368",
        LA_name="West Sussex",
        LA_pr="https://www.westsussex.gov.uk/news",
    links="https://www.westsussex.gov.uk/news",
    listas=".row > .col.small_6, .row.push-half--bottom",
    datesss="time",
    replaceDate=None,
    title="h2",
    getBody=getBody,
    content="article > p:not(:first-child)",
    imajina="sam",
    imajinasi="img",
    linkedin="https://www.westsussex.gov.uk",
    href="a",
    linkedin2="https://www.westsussex.gov.uk")


