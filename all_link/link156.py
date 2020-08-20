
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link156():
    getList(
    pagis=0,
    numero="156",
    LA_name="East Hampshire",
    LA_pr="https://www.easthants.gov.uk/latest-news",
    links="https://www.easthants.gov.uk/latest-news?page=",
    listas=".view-content>*",
    datesss=".view-content>div>div.views-field.views-field-stamp",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".view-content>div>span.views-field.views-field-title>h4",
    getBody=getBody,
    content=".node-content>div>div>div>*:not(.date-display-single)",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.easthants.gov.uk",
    href=".view-content>div>span.views-field.views-field-title>h4>a",
    linkedin2="https://www.easthants.gov.uk")


