import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link67():
    getList(
    numero="67",
    LA_name="Tendring",
    LA_pr="https://www.tendringdc.gov.uk/council/latest-council-news",
    links="https://www.tendringdc.gov.uk/feeds/news/news.rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="div.field.field-name-body.field-type-text-with-summary.field-label-hidden.view-mode-full > div > div",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
