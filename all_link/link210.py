
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link210():
    getList(
    pagis=1,
    numero="210",
    LA_name="Lichfield",
    LA_pr="https://www.lichfielddc.gov.uk/news",
    links="https://www.lichfielddc.gov.uk/news?page=",
    listas=".page-content > ul > .list__item",
    datesss=".meta--date",
    replaceDate="Published: ",
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content=".page-content > *:not(h1)",
    imajina=".page-content > img",
    imajinasi="sam",
    linkedin="https://www.lichfielddc.gov.uk",
    href="a",
    linkedin2="https://www.lichfielddc.gov.uk")


