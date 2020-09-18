
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link197():
    getList(
    pagis=1,
    numero="197",
    LA_name="Scotland",
    LA_pr="https://www.gov.scot/news/",
    links="https://www.gov.scot/news/?cat=filter&page=",
    listas=".listed-content-item__article",
    datesss=".listed-content-item__date",
    replaceDate="|",
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content=".body-content",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.gov.scot",
    href="a",
    linkedin2="")


