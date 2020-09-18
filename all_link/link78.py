
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse

from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link78():
    getList(
        datea=None,
        getDatea=None,
numero="78",
    LA_name="Rochdale",
    LA_pr="http://www.rochdale.gov.uk/news/",
    links="http://www.rochdale.gov.uk/news/",
    listas="#newsContainer > .article",
    datesss=".date",
    replaceDate=None,
    title=".title",
    getBody=getBody,
    content="#ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField",
    imajina="#ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField > p > img",
    linkedin="http://www.rochdale.gov.uk",
    href="a",
    linkedin2="http://www.rochdale.gov.uk")
