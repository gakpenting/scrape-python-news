
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link304():
    getList(
        datea=None,
        getDatea=None,
numero="304",
        LA_name="Nottinghamshire",
        LA_pr="https://www.nottinghamshire.gov.uk/newsroom/news",
    links="https://www.nottinghamshire.gov.uk/newsroom/news",
    listas=".news-snippet-item",
    datesss=".news-snippet-date",
    replaceDate=None,
    title=".news-snippet-title",
    getBody=getBody,
    content=".news-article-pad > p",
    imajina=".news-article-thumbnail",
    linkedin="",
    href="a",
    linkedin2="https://www.nottinghamshire.gov.uk")
