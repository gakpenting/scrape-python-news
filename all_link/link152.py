
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link152():
    getList(
    pagis=0,
    numero="152",
    LA_name="Waltham Forest",
    LA_pr="https://walthamforest.gov.uk/news",
    links="https://www.walthamforest.gov.uk/media?page=",
    listas="#block-system-main>div>.view-content>div.views-row",
    datesss="#block-system-main>div>.view-content>div.views-row>div.views-field.views-field-nothing-1>span>.views-field-created",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="#block-system-main>div>.view-content>div.views-row>div.views-field.views-field-nothing-1>span>h2",
    getBody=getBody,
    content="#block-system-main>article>div.field.field-name-body>*>*>*",
    imajina="#block-system-main>article> div.field.field-name-field-header-image>div>div>img",
    imajinasi="sam",
    linkedin="https://walthamforest.gov.uk",
    href="#block-system-main>div>.view-content>div.views-row>div.views-field.views-field-nothing-1>span>h2>span>a",
    linkedin2="")


