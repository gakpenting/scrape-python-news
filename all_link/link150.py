
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link150():
    getList(
        datea="None",
        getDatea=getDate,
numero="150",
    LA_name="Richmond upon Thames",
    LA_pr="https://www.richmond.gov.uk/council/news",
    links="https://www.richmond.gov.uk/council/news",
    listas=".lb-article-holder",
    datesss="date",
    replaceDate=None,
    title="h1",
    getBody=getBody,
    content=".article__body > div > div > p",
    imajina=".article__body > div > div > img",
    linkedin="http://www.southkesteven.gov.uk/",
    href="a",
    linkedin2="http://www.southkesteven.gov.uk/")



