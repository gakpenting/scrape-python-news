
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link188():
    getList(
    pagis=0,
    numero="188",
    LA_name="Corby",
    LA_pr="https://www.corby.gov.uk/latest-news",
    links="https://www.corby.gov.uk/latest-news?keys=&page=",
    listas="li.views-row",
    datesss=".date-display-single",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".views-field-title",
    getBody=getBody,
    content="div[property='content:encoded']",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.corby.gov.uk",
    href="a",
    linkedin2="")


