
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link354():
    getList(
        datea=None,
        getDatea=None,
numero="354",
        LA_name="Denbighshire",
        LA_pr="https://www.denbighshire.gov.uk/en/resident/news/news.aspx",
    links="https://www.denbighshire.gov.uk/en/resident/news/news.aspx",
    listas="#NewsListing_List > div > div",
    datesss="dd.sys_news-datepublished",
    replaceDate=None,
    title="h5",
    getBody=getBody,
    content="#content > div:nth-child(3) > div.col6.article > div > div",
    imajina="sam",
    linkedin="https://www.denbighshire.gov.uk",
    href="a",
    linkedin2="")


