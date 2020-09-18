
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link158():
    getList(
    pagis=0,
    numero="158",
    LA_name="Havant",
    LA_pr="https://www.havant.gov.uk/latest-news",
    links="https://www.havant.gov.uk/latest-news?page=",
    listas=".view-content>div",
    datesss=None,
    replaceDate=None,
    replaceRegex=None,
    datea=".node-content>div.field.field-name-field-news-date.field-type-datestamp>div>*",
    getDatea=getDate,
    title=".view-content>div>span>h4",
    getBody=getBody,
    content=".node-content>div.field.field-name-body.field-type-text-with-summary>div>div>*",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.havant.gov.uk",
    href=".view-content>div>span>h4>a",
    linkedin2="https://www.havant.gov.uk")


