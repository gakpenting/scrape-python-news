
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link207():
    getList(
    pagis=1,
    numero="207",
    LA_name="Somerset West and Taunton",
    LA_pr="https://www.somersetwestandtaunton.gov.uk/news/",
    links="https://www.somersetwestandtaunton.gov.uk/news/?page=",
    listas="body > main > div.container.mt-5 > div > div.col-md-8 > div > div",
    datesss="p.date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content="body > main > div.container.mt-5 > div > div.col-md-8 > *:not(h1):not(.title-date)",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.somersetwestandtaunton.gov.uk",
    href="a",
    linkedin2="")


