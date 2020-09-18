
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link412():
    getList(
        datea=None,
        getDatea=None,
numero="412",
LA_name="Shetland Islands",
LA_pr="shetland.gov.uk/news",
    links="http://shetland.gov.uk/news-advice/info-bulletins.asp",
    listas=".tableheader",
    datesss="th",
    replaceDate=None,
    title="th.tableheader > div > a",
    getBody=getBody,
    content="#content div  p",
    imajina="#content div p img",
    linkedin="http://shetland.gov.uk/news-advice/",
    href="a",
    linkedin2="http://shetland.gov.uk/news-advice/",
    dayfirst=True
    )


