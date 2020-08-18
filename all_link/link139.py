
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link139():
    getList(
    pagis=1,
    numero="139",
    LA_name="Chiltern",
    LA_pr="https://www.chiltern.gov.uk/article/8020/News", 
    links="https://www.chiltern.gov.uk/news-press-releases?p=", 
    listas="ol > li:not(.socialmedia__item):not(.sitemenu__item):not(.utilitymenu__item)", 
    datesss=None, 
    replaceDate=None,
    replaceRegex=None,
    datea="",
    getDatea=getDate,
    title="h2",
    getBody=getBody,
    content="div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div > *",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.thurrock.gov.uk",
    href="a",
    linkedin2="https://www.thurrock.gov.uk")


