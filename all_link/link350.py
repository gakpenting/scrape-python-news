
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link350():
    getList(
        datea=None,
        getDatea=None,
  numero="350",
        LA_name="Caerphilly",
        LA_pr="https://www.caerphilly.gov.uk/News.aspx",
    links="https://www.caerphilly.gov.uk/News.aspx",
    listas="#wrapper > div.container > div > div:nth-child(3) > div > div > ul > li",
    datesss=".date",
    replaceDate=None,
    title=".title",
    getBody=getBody,
    content=".news-summary",
    imajina=".story_image > img",
    linkedin="https://www.caerphilly.gov.uk",
    href="a",
    linkedin2="https://www.caerphilly.gov.uk")


