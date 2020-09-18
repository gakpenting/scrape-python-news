
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link417():
    getList(
        datea=None,
        getDatea=None,
numero="417",
LA_name="Sutton",
LA_pr="sutton.gov.uk/news",
    links="https://www.sutton.gov.uk/news",
    listas="#content > ul > li",
    datesss=".listing__meta.listing__meta--date",
    replaceDate=None,
    title="h2",
    getBody=getBody,
    content=".page-content > p:not(.date)",
    imajina="sam",
    linkedin="",
    href="a",
    linkedin2="")


