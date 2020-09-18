
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link297():
    getList(
        datea=None,
        getDatea=None,
numero="297",
        LA_name="Northampton",
        LA_pr="https://www.northampton.gov.uk/news",
    links="https://www.northampton.gov.uk/news",
    listas="article.listing",
    datesss=".listing__meta--date",
    replaceDate=None,
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    title="h2",
    getBody=getBody,
    content=".lead, .editor",
    imajina="sam",
    linkedin="",
    href="a",
    linkedin2="")

