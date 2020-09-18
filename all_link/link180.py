
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link180():
    getList(
    pagis=1,
    numero="180",
    LA_name="Lincoln",
    LA_pr="https://www.lincoln.gov.uk/news",
    links="https://www.lincoln.gov.uk/news?page=",
    listas="#content > div > ul > li> article ",
    datesss="#content > div > ul > li> article > a > div > div > p",
    replaceDate="Published on",
    replaceRegex=None,
    getDatea=None,
    title="#content > div > ul > li > article > a > div > h2",
    getBody=getBody,
    content=".page-content>.summary,.editor",
    imajina=".page-content>img",
    imajinasi="sam",
    linkedin="https://www.lincoln.gov.uk",
    href="#content > div > ul > li > article > a",
    linkedin2="https://www.lincoln.gov.uk")


