
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate as getDatea,getBody
import re
def link143():
    getList(
    pagis=1,
    numero="143",
    LA_name="Uttlesford",
    LA_pr="https://www.uttlesford.gov.uk/news",
    links="https://www.uttlesford.gov.uk/news?p=",
    listas="div.item__content > ol > div > li",
    datesss=None,
    replaceDate=None,
    replaceRegex=None,
    getDatea=getDatea,
    datea="#maincontent > div > div.a-body.a-body--default > p:last-child",
    title="a",
    getBody=getBody,
    content=".a-body > p:not(:last-child)",
    imajina="#maincontent > div > div.a-relimage.a-relimage--default > img",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")


