
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link208():
    getList(
    pagis=1,
    numero="208",
    LA_name="Rotherham",
    LA_pr="https://www.rotherham.gov.uk/news",
    links="https://www.rotherham.gov.uk/news?page=",
    listas=".page-content > ul > li",
    datesss=".meta--date",
    replaceDate="Published: ",
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content=".page-content",
    imajina=".page-content > img",
    imajinasi="sam",
    linkedin="https://www.rotherham.gov.uk",
    href="a",
    linkedin2="https://www.rotherham.gov.uk")


