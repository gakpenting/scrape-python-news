import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link35():
    getList(
    pagis=0,
    numero="35",
    LA_name="Copeland",
    LA_pr="https://www.copeland.gov.uk/news",
    links="https://www.copeland.gov.uk/news?page=",
    listas="#block-system-main > div > div > div > div.view-content > div.views-row",
    datesss=".press-release__date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h3",
    getBody=getBody,
    content="div[property='content:encoded']",
    imajina="div > div > img",
    imajinasi="sam",
    linkedin="https://www.copeland.gov.uk",
    href="a",
    linkedin2="")

