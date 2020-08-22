
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link175():
    getList(
    pagis=1,
    numero="175",
    LA_name="Leicestershire",
    LA_pr="https://www.leicestershire.gov.uk/news",
    links="https://www.leicestershire.gov.uk/news?page=",
    listas="#block-system-main > div > div > div > div.column-10.column-indent-1 > div > ul > li",
    datesss="#block-system-main > div > div > div > div.column-10.column-indent-1 > div > ul > li > div > div > div:nth-child(2) > span",
    replaceDate="Date:",
    replaceRegex=None,
    getDatea=None,
    title="#block-system-main > div > div > div > div.column-10.column-indent-1 > div > ul > li > div > h3",
    getBody=getBody,
    content="#block-system-main > div > div > article > div > div.column-10 > div:nth-child(2) > div > div > div>*",
    imajina="#block-system-main > div > div > article > div > div.column-10 > div:nth-child(1) > figure > img",
    imajinasi="sam",
    linkedin="https://www.leicestershire.gov.uk",
    href="#block-system-main > div > div > div > div.column-10.column-indent-1 > div > ul > li > div > h3>a",
    linkedin2="")


