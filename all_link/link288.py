
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link288():
    getList(
        datea=None,
        getDatea=None,
numero="288",
        LA_name="Norfolk",
        LA_pr="https://www.norfolk.gov.uk/news",
    links="https://www.norfolk.gov.uk/news",
    listas=".search-list > li",
    datesss="p > strong",
    replaceDate=None,
    title="strong",
    getBody=getBody,
    content=".page-content > p:not(:nth-child(2)), .page-content > li",
    imajina="sam",
    linkedin="",
    href="a",
    linkedin2="")

