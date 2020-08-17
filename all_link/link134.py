
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link134():
    getList(
    numero="134",
    LA_name="Worthing",
    LA_pr="https://www.adur-worthing.gov.uk/news/",
    links="https://www.adur-worthing.gov.uk/news/rss/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#page-content>*:not(:nth-child(1)):not(:nth-child(2)):not(.back-to-top):not(.jump-menu-see-also):not(#contact-details):not(.button-link)",
    imajina="#page-content>* >img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.adur-worthing.gov.uk")

