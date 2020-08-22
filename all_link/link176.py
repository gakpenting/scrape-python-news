
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link176():
    getList(
    pagis=1,
    numero="176",
    LA_name="Leicester",
    LA_pr="https://news.leicester.gov.uk/",
    links="https://news.leicester.gov.uk/?page=",
    listas="#news-section > div.columns.small-12.medium-9.large-9.news-items.page-content > ul > li",
    datesss="#news-section > div.columns.small-12.medium-9.large-9.news-items.page-content > ul > li > div > div.news-item-content > span.muted",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="#news-section > div.columns.small-12.medium-9.large-9.news-items.page-content > ul > li > div > div.news-item-content > span.h4",
    getBody=getBody,
    content="body > div.off-canvas-wrap > div > main > div > div > div.small-12.medium-9.columns.page-content>*:not(:nth-child(2)):not(h1):not(img)",
    imajina="body > div.off-canvas-wrap > div > main > div > div > div.small-12.medium-9.columns.page-content>img",
    imajinasi="sam",
    linkedin="https://news.leicester.gov.uk",
    href="#news-section > div.columns.small-12.medium-9.large-9.news-items.page-content > ul > li > div > a",
    linkedin2="https://news.leicester.gov.uk")


