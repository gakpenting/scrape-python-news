
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link145():
    getList(
    pagis=1,
    numero="145",
    LA_name="Hammersmith and Fulham",
    LA_pr="https://www.lbhf.gov.uk/allnews",
    links="https://www.lbhf.gov.uk/allnews?page=",
    listas="#main > div > div > div > section > div > ul > li",
    datesss="time",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="a",
    getBody=getBody,
    content=".body>*:not(.media)",
    imajina=".header__article > * > img",
    imajinasi="sam",
    linkedin="https://www.lbhf.gov.uk",
    href="a",
    linkedin2="")


