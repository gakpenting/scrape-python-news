
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link283():
    getList(
        datea=".single-datetime",
        getDatea=getDate,
    numero="283",
        LA_name="North East Lincolnshire",
        LA_pr="https://www.nelincs.gov.uk/?s=news",
    links="https://www.nelincs.gov.uk/news/",
    listas=".all-news-post",
    datesss=".post-title",
    replaceDate=None,
    title=".post-title",
    getBody=getBody,
    content=".single-post > p",
    imajina=".single-featured > img",
    linkedin="",
    href="a",
    linkedin2="")

