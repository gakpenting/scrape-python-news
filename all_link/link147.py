
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link147():
    getList(
    pagis=1,
    numero="147",
    LA_name="Hillingdon",
    LA_pr="https://www.hillingdon.gov.uk/article/2036/News-in-Hillingdon",
    links="https://www.hillingdon.gov.uk/article/2036/News-in-Hillingdon?p=",
    listas="div.grid__cell--news",
    datesss="div>div>div>.pa-block__details>div.pa-block__info",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="div>div>div>.pa-block__details>div.pa-block__title>a",
    getBody=getBody,
    content=".a-body__inner>*",
    imajina="sam",
    imajinasi="div.grid__cell--news>div>div>div>div.pa-block__imagecontainer>a>img",
    linkedin="https://www.hillingdon.gov.uk",
    href="a",
    linkedin2="https://www.hillingdon.gov.uk")


