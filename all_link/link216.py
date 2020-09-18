
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link216():
    getList(
    pagis=1,
    numero="216",
    LA_name="Powys",
    LA_pr="https://en.powys.gov.uk/news",
    links="https://en.powys.gov.uk/news?p=",
    listas=".item__title",
    datesss=None,
    replaceDate=None,
    replaceRegex=None,
    datea=".a-body__inner > p:first-child",
    getDatea=getDate,
    title="h2",
    getBody=getBody,
    content=".a-body__inner > *:not(:first-child)",
    imajina=".a-body__inner img",
    imajinasi="sam",
    linkedin="https://en.powys.gov.uk",
    href="a",
    linkedin2="https://en.powys.gov.uk")


