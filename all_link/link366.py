
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link366():
    getList(
        datea=None,
        getDatea=None,
 numero="366",
        LA_name="West Midlands",
        LA_pr="https://www.wmca.org.uk/news",
    links="https://www.wmca.org.uk/news",
    listas="article",
    datesss="time.date",
    replaceDate=None,
    title="h3",
    getBody=getBody,
    content=".copy",
    imajina=".copy > img",
    linkedin="https://www.wmca.org.uk",
    href="a",
    linkedin2="https://www.wmca.org.uk")


