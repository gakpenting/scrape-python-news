
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link174():
    getList(
    pagis=1,
    numero="174",
    LA_name="Preston",
    LA_pr="https://www.preston.gov.uk/news",
    links="https://www.preston.gov.uk/news?p=",
    listas="#maincontent > div > div > div.grid.grid--list.grid--1col > div",
    datesss=None,
    replaceDate=None,
    replaceRegex=None,
      getDatea=getDate,
    datea="#maincontent > div > div > div.a-body.a-body--default > p:nth-child(2)",
    title="div > div > div.item__content > div.item__title > a",
    getBody=getBody,
    content="#maincontent > div > div > div.a-body.a-body--default>*>*:not(img):not(strong)",

    imajina="sam",
    imajinasi="#maincontent > div > div > div.grid.grid--list.grid--1col > div:nth-child(1) > div > div > div.item__imagecontainer > img",
    linkedin="",
    href="div > div > div.item__content > div.item__title > a",
    linkedin2="")


