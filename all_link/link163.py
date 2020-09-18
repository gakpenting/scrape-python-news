
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link163():
    getList(
    pagis=0,
    numero="163",
    LA_name="North Hertfordshire",
    LA_pr="https://www.north-herts.gov.uk/latest-news",
    links="https://www.north-herts.gov.uk/latest-news?page=",
    listas="#block-system-main>div>div>div.view-content>*",
    # datesss="#block-system-main>div>div>div.view-content>div>article>div.field.field-name-field-pr-date.field-type-datetime.field-label-hidden",
datesss=None,
    replaceDate=None,
    replaceRegex=None,
    datea="#block-system-main>div>div>div>div>.field-name-field-pr-date>div.field-items",
    getDatea=getDate,
    title="#block-system-main>div>div>div.view-content>div>article>header>h2",
    getBody=getBody,
    content="#block-system-main>div>div>div>div>div:not(.field-name-field-pr-date):not(.field-name-field-image-file)",
    imajina="#block-system-main>div>div>div>div>.field-name-field-image-file>div>div>img",
    imajinasi="sam",
    linkedin="https://www.north-herts.gov.uk",
    href="#block-system-main>div>div>div.view-content>div>article>header>h2>a",
    linkedin2="")


