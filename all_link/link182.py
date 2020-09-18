
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link182():
    getList(
    pagis=1,
    numero="182",
    LA_name="South Holland",
    LA_pr="https://www.sholland.gov.uk/News",
    links="https://www.sholland.gov.uk/News?p=",
    listas="body > main > article > div > div.grid.grid--list.grid--1col > div",
    datesss=None,
    replaceDate="Posted on",
    replaceRegex=None,
    datea="body > main > article > div > div.a-body.a-body--default > p:nth-child(1) > strong",
    getDatea=getDate,
    title="body > main > article > div > div.grid.grid--list.grid--1col > div > div > div > div.item__content > div.item__title > a",
    getBody=getBody,
    content="body > main > article > div > div.a-body.a-body--default>*:not(:first-child)",
    imajina="body > main > article > div > div.a-body.a-body--default > p> img",
    imajinasi="sam",
    linkedin="",
    href="body > main > article > div > div.grid.grid--list.grid--1col > div > div > div > div.item__content > div.item__title > a",
    linkedin2="")


