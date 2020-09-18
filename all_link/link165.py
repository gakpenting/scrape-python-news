
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link165():
    getList(
    pagis=1,
    numero="165",
    LA_name="Isle of Wight",
    LA_pr="https://www.iow.gov.uk/news/",
    links="https://www.iow.gov.uk/news/default.aspx?page=",
    listas="#newsArchive > div ",
    datesss=".newsDate",
    replaceDate=None,
    replaceRegex="\d+\s\w+\s\d{1,} ",
    #  replaceRegex="(?=Last updated at).+",
    getDatea=None,
    title="a",
    getBody=getBody,
    content="#newsContentLeft >p",
    imajina="#imgMedia",
    imajinasi="sam",
    linkedin="https://www.iow.gov.uk",
    href="a",
    linkedin2="https://www.iow.gov.uk")
