
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link204():
    getList(
    pagis=1,
    numero="204",
    LA_name="Telford and Wrekin",
    LA_pr="http://newsroom.telford.gov.uk/",
    links="http://newsroom.telford.gov.uk/?grid-page=",
    listas=".grid-row",
    datesss=".newsItem > div.col-sm-9> div > div > span:nth-child(1)",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h5 > a",
    getBody=getBody,
    content="#content",
    imajina="#mainImg > img",
    imajinasi="sam",
    linkedin="http://newsroom.telford.gov.uk",
    href="a",
    linkedin2="")


