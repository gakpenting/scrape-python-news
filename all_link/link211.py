
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link211():
    getList(
    pagis=1,
    numero="211",
    LA_name="Elmbridge",
    LA_pr="https://www.elmbridge.gov.uk/news/",
    links="https://www.elmbridge.gov.uk/news/?lister399p=",
    listas="ul.gamma > li",
    datesss=None,
    replaceDate=None,
    replaceRegex=None,
    datea="head > meta[name='Date']",
    getDatea=getDate,
    title=".item-ttl",
    getBody=getBody,
    content="div.contenteditor > *:not(h1):not(h2):not(ul)",
    imajina="sam",
    imajinasi=".item-img > img",
    linkedin="https://www.elmbridge.gov.uk",
    href="a",
    linkedin2="https://www.elmbridge.gov.uk")


