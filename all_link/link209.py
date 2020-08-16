
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link209():
    getList(
    pagis=1,
    numero="209",
    LA_name="Cannock Chase",
    LA_pr="https://www.cannockchasedc.gov.uk/council/latest-news",
    links="https://www.cannockchasedc.gov.uk/council/latest-news?page=",
    listas=".view-content > *",
    datesss=".date",
    replaceDate=None,
    replaceRegex=r"\w+\s",
    getDatea=None,
    title=".title",
    getBody=getBody,
    content=".contleft > *:not(.eventtitle):not(.eventdesc)",
    imajina=".img > img",
    imajinasi="sam",
    linkedin="https://www.cannockchasedc.gov.uk",
    href="a",
    linkedin2="")


