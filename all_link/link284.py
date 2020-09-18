
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link284():
    getList(
        datea=".post-timedate",
        getDatea=getDate,
    numero="284",
        LA_name="North Lincolnshire",
        LA_pr="https://www.northlincs.gov.uk/news/",
    links="https://www.northlincs.gov.uk/news/",
    listas=".news-post",
    datesss=".post-title",
    replaceDate=None,
    title=".post-title",
    getBody=getBody,
    content=".single-content > p",
    imajina=".single-featured > img",
    linkedin="",
    href="a",
    linkedin2="")

