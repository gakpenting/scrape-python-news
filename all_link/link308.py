
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link308():
    getList(
        datea="#mainContent > div",
        getDatea=getDate,
numero="308",
        LA_name="Newark and Sherwood",
        LA_pr="https://www.newark-sherwooddc.gov.uk/#horizontalTab3",
    links="https://www.newark-sherwooddc.gov.uk/#horizontalTab3",
    listas=".blogheader",
    datesss="h2",
    replaceDate=None,
    title="h2",
    getBody=getBody,
    content="#mainContent > p",
    imajina="sam",
    linkedin="https://www.newark-sherwooddc.gov.uk",
    href="a",
    linkedin2="")


