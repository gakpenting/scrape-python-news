
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link203():
    getList(
    pagis=1,
    numero="203",
    LA_name="Stirling",
    LA_pr="https://www.stirling.gov.uk/news/",
    links="https://www.stirling.gov.uk/news/?page=",
    listas=".news-item",
    datesss=".card-subtitle",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h5",
    getBody=getBody,
    content=".page-content > p",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.stirling.gov.uk",
    href="a",
    linkedin2="")


