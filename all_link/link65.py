import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link65():
    getList(
        pagis=1,
    numero="65",
    LA_name="Harlow",
    LA_pr="https://www.harlow.gov.uk/news",
    links="https://www.harlow.gov.uk/news?page=",
    listas="div.views-row",
    datesss="time",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="span.field-content",
    getBody=getBody,
    content="body > div > div.main-container.container.js-quickedit-main-content > div > section > article > div > div.field.field--name-body.field--type-text-with-summary.field--label-hidden.field--item",
    imajina="sam",
    imajinasi="img",
    linkedin="https://www.harlow.gov.uk",
    href="a",
    linkedin2="https://www.harlow.gov.uk")
