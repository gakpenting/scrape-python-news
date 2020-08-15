
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link213():
    getList(
    pagis=1,
    numero="213",
    LA_name="South Tyneside",
    LA_pr="https://www.southtyneside.gov.uk/article/55009/News",
    links="https://www.thurrock.gov.uk/news?page=",
    listas="div.views-row",
    datesss=".date-display-single",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content="div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div > *",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.thurrock.gov.uk",
    href="a",
    linkedin2="https://www.thurrock.gov.uk")


