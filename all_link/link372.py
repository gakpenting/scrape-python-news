
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link372():
    getList(
        datea=None,
        getDatea=None,
numero="372",
        LA_name="West Yorkshire",
        LA_pr="https://www.westyorks-ca.gov.uk/news/",
    links="https://www.westyorks-ca.gov.uk/news/",
    listas="article",
    datesss=".card-tags__item",
    replaceDate=None,
    title="h3",
    getBody=getBody,
    content=".wysiwyg-block",
    imajina="sam",
    imajinasi="div.card__img-holder > picture > img",
    linkedin="",
    href="a",
    linkedin2="https://www.westyorks-ca.gov.uk")



