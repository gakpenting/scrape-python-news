
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link206():
    getList(
    pagis=1,
        numero="206",
    LA_name="Mendip",
    LA_pr="https://www.mendip.gov.uk/news",
    links="https://www.mendip.gov.uk/news?p=",
    listas=".item__sublinks > li",
    datesss="div",
    replaceDate=None,
    replaceRegex=None,
    getDatea=getDate,
    datea="",
    title="h2",
    getBody=getBody,
    content="div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div > *",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.thurrock.gov.uk",
    href="a",
    linkedin2="https://www.thurrock.gov.uk")


