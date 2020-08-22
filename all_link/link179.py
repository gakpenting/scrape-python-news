
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link179():
    getList(
    pagis=1,
    numero="179",
    LA_name="East Lindsey",
    LA_pr="https://www.e-lindsey.gov.uk/article/4986/Latest-News",
    links="https://www.e-lindsey.gov.uk/article/4986/Latest-News?p=",
    listas="div.grid.grid--list.grid--1col > div",
    datesss=None,
    replaceDate="",
    replaceRegex=None,
    datea="body > main > article > div > p",
    getDatea=getDate,
    title="body > main > article > div > div.grid.grid--list.grid--1col > div > div > div > div.item__content > div.item__title > a",
    getBody=getBody,
    content="body > main > article > div > div.a-body.a-body--default>*",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="body > main > article > div > div.grid.grid--list.grid--1col > div> div > div > div.item__content > div.item__title > a",
    linkedin2="")


