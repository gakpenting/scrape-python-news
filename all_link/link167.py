
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link167():
    getList(
    pagis=1,
    numero="167",
    LA_name="Canterbury",
    LA_pr="https://news.canterbury.gov.uk/news",
    links="https://news.canterbury.gov.uk/news?page=",
    listas="#content > ul > li",
    datesss="#content > ul > li > article > a > div > div.col-8 > div > div > p",
    replaceDate="Published: ",
    replaceRegex=None,
    getDatea=None,
    title="#content > ul > li > article > a > div > div.col-8 > div > h2",
    getBody=getBody,
    content="#content > div.editor>*",
    imajina="#content > span > img",
    imajinasi="sam",
    linkedin="https://news.canterbury.gov.uk",
    href="#content > ul > li > article > a",
    linkedin2="https://news.canterbury.gov.uk")


