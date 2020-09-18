
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link330():
    getList(
        datea=None,
        getDatea=None,
numero="330",
        LA_name="South Somerset",
        LA_pr="https://www.southsomerset.gov.uk/news",
    links="https://www.southsomerset.gov.uk/news",
    listas=".teaser.latest-news",
    datesss="time",
    replaceDate=None,
    title="h3",
    getBody=getBody,
    content="article > p",
    imajina="sam",
    linkedin="https://www.southsomerset.gov.uk",
    href="a",
    linkedin2="")


