
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link190():
    getList(
    pagis=1,
    numero="190",
    LA_name="Belfast",
    LA_pr="http://www.belfastcity.gov.uk/News/News.aspx",
    links="https://www.belfastcity.gov.uk/news?page=",
    listas="#maincontent > div > div > div > div.cell.large-9.medium-8 > div > div.grid-x.grid-padding-x.medium-up-2 > div.cell",
    datesss=".event-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".title-bold",
    getBody=getBody,
    content="article > p:not(:first-child)",
    imajina="article > img",
    imajinasi="sam",
    linkedin="https://www.belfastcity.gov.uk",
    href="a",
    linkedin2="https://www.belfastcity.gov.uk")


