
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link184():
    getList(
    pagis=1,
    numero="184",
    LA_name="St. Helens",
    LA_pr="https://www.sthelens.gov.uk/news/",
    links="https://www.sthelens.gov.uk/news?page=",
    listas="body > div.container > div.row > div > div > div",
    datesss="a",
    replaceDate=None,
    replaceRegex="\d{1,2}\/\d{1,2}\/\d{4}",
    dayfirst=True,
    datea=None,
    getDatea=None,
    title="a",
    getBody=getBody,
    content="body > div.container > *:not(h2):not(p)",
    imajina="body > div.container > img",
    imajinasi="sam",
    linkedin="",
    href="body > div.container > div.row > div > div > div > a",
    linkedin2="https://www.sthelens.gov.uk")


