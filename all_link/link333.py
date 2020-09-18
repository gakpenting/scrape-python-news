
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link333():
    getList(
        datea=".field-type-datetime",
        getDatea=getDate,
numero="333",
        LA_name="East Staffordshire",
        LA_pr="http://www.eaststaffsbc.gov.uk/es-news",
    links="http://www.eaststaffsbc.gov.uk/es-news",
    listas=".view-content > .views-row",
    datesss="div",
    replaceDate=None,
    title=".field-content",
    getBody=getBody,
    content="div[property='content:encoded']",
    imajina="sam",
    imajinasi=".field-content > img",
    linkedin="http://www.eaststaffsbc.gov.uk",
    href="a",
    linkedin2="")


