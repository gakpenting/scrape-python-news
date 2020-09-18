
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link177():
    getList(
    pagis=1,
    numero="177",
    LA_name="Lincolnshire",
    LA_pr="https://www.lincolnshire.gov.uk/news",
    links="https://www.lincolnshire.gov.uk/news?page=",
    listas="#content > div > ul > li",
    datesss="#content > div > ul > li > article > a > div > div > p",
    replaceDate="Published:",
    replaceRegex=None,
    getDatea=None,
    title="#content > div > ul > li > article > a > div > h2",
    getBody=getBody,
    content="#content > div > div.editor>*",
    imajina="#content > div > img",
    imajinasi="sam",
    linkedin="https://www.lincolnshire.gov.uk",
    href="#content > div > ul > li > article > a",
    linkedin2="https://www.lincolnshire.gov.uk")


