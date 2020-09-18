
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link157():
    getList(
    pagis=1,
    numero="157",
    LA_name="Gosport",
    LA_pr="https://www.gosport.gov.uk/pressreleases",
    links="https://www.gosport.gov.uk/pressreleases?p=",
    listas=".item__content",
    datesss=".item__body",
    replaceDate=None,
    replaceRegex="^\d{1,2}\s\w+\s\d{4}",
    getDatea=None,
    title=".item__link",
    getBody=getBody,
    content=".a-body",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")


