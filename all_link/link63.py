import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link63():
    getList(
        pagis=1,
    numero="63",
    LA_name="Castle Point",
    LA_pr="https://www.castlepoint.gov.uk/news",
    links="https://www.castlepoint.gov.uk/news/?pag_page=",
    listas=".list-content-item",
    datesss=".item-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h3",
    getBody=getBody,
    content="#placement-7-1 > div > div > div > div > div > div.content-wrapper-inner > div",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.castlepoint.gov.uk",
    href="a",
    linkedin2="")
