import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link64():
    getList(
        pagis=1,
    numero="64",
    LA_name="Chelmsford",
    LA_pr="https://www.chelmsford.gov.uk/news/",
    links="https://www.chelmsford.gov.uk/news/?lister3383p=",
    listas="div.pel-i > div.bdo:nth-of-type(2) > div.bdi > ul.oBoxList > li.oBoxItem",
    datesss="span.item-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="span.item-title",
    getBody=getBody,
    content="#-ux-content > div.pel-outer.columns-outer.columns-alpha > div > div > div.column-outer.column-alpha > div > div > div:nth-child(2)",
    imajina="sam",
    imajinasi="img",
    linkedin="https://www.chelmsford.gov.uk",
    href="a",
    linkedin2="https://www.chelmsford.gov.uk")
