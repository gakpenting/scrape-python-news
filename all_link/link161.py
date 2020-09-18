
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link161():
    getList(
    pagis=0,
    numero="161",
    LA_name="East Hertfordshire",
    LA_pr="https://www.eastherts.gov.uk/latest-news",
    links="https://www.eastherts.gov.uk/latest-news?page=",
    listas=".view.view-news.view-id-news>div>*",
    datesss=".view.view-news.view-id-news>div>div>article>div>div>div>div>div.layout__region.layout__region--second.col>div>div>span.field.field--name-created.field--type-created.field--label-hidden",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".view.view-news.view-id-news>div>div>article>div>div>div>div>div.layout__region.layout__region--second.col>div>div>span.field.field--name-title.field--type-string.field--label-hidden",
    getBody=getBody,
    content=".content>div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item>p",
    imajina="sam",
    imajinasi=".view.view-news.view-id-news>div>div>article>div>div>div>div>div.layout__region.layout__region--first.col>div>div>div>img",
    linkedin="https://www.eastherts.gov.uk",
    href=".view.view-news.view-id-news>div>div>article>div>div>div>div>div.layout__region.layout__region--second.col>div>div>span.field.field--name-title.field--type-string.field--label-hidden>a",
    linkedin2="https://www.eastherts.gov.uk")


