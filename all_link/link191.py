
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link191():
    getList(
    pagis=1,
    numero="191",
    LA_name="Derry City and Strabane",
    LA_pr="https://www.derrystrabane.com/Council/News",
    links="https://www.derrystrabane.com/Council/News?page=",
    listas=".listing-item",
    datesss=".listing-item-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h1",
    getBody=getBody,
    content=".lower-col-right > p",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.derrystrabane.com",
    href="a",
    linkedin2="")


