
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
    datesss=None,
    replaceDate="Article date -",
    replaceRegex=None,
    datea="body > div.container > p:nth-child(2)",
    getDatea=getDate,
    title="body > div.container > div.row > div > div > div > a",
    getBody=getBody,
    content="body > div.container > *:not(:first-child):not(:nth-child(2)):not(div):not(img)",
    imajina="body > div.container > img",
    imajinasi="sam",
    linkedin="https://www.sthelens.gov.uk",
    href="body > div.container > div.row > div > div > div > a",
    linkedin2="https://www.sthelens.gov.uk")


