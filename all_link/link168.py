
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link168():
    getList(
    pagis=1,
    numero="168",
    LA_name="Dartford",
    LA_pr="https://www.dartford.gov.uk/news",
    links="https://www.dartford.gov.uk/news?result_1468_result_page=",
    listas="#content > main > div.indexes > ul > li",
    datesss="p[style='text-align:right;margin-top:12px;']",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="strong",
    getBody=getBody,
    content=".desc > p",
    imajina="sam",
    imajinasi="img",
    linkedin="https://www.dartford.gov.uk/",
    href="a",
    linkedin2="")




