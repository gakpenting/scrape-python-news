
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link213():
    getList(
    pagis=1,
    numero="213",
    LA_name="South Tyneside",
    LA_pr="https://www.southtyneside.gov.uk/article/55009/News",
    links="https://www.southtyneside.gov.uk/article/55009/News?p=",
    listas=".item",
    datesss="time",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="a > span",
    getBody=getBody,
    content=".id-content-bottom > *:not(time):not(.snippet):not(.id-govmetric)",
    imajina="img.main",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")


