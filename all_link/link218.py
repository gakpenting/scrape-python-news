
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link218():
    getList(
    pagis=0,
    numero="218",
    LA_name="Wolverhampton",
    LA_pr="https://www.wolverhampton.gov.uk/news",
    links="https://www.wolverhampton.gov.uk/news?page=",
    listas=".view-content > .views-row",
    datesss="time.datetime",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h3",
    getBody=getBody,
    content="#block-omega-bigbluedoor-content > div > article",
    imajina="#block-entityviewcontent > div > article > div > div > div > article > div.field.field--name-field-media-image.field--type-image.field--label-hidden.field__item > img",
    imajinasi="sam",
    linkedin="https://www.wolverhampton.gov.uk",
    href="a",
    linkedin2="https://www.wolverhampton.gov.uk")


