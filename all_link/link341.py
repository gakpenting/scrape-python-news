
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link341():
    getList(
        datea=None,
        getDatea=None,
numero="341",
        LA_name="Epsom and Ewell",
        LA_pr="https://www.epsom-ewell.gov.uk/news",
    links="https://www.epsom-ewell.gov.uk/news",
    listas="tbody > tr",
    datesss=".date-display-single",
    replaceDate=None,
    title=".views-field",
    getBody=getBody,
    content="div[property='content:encoded']",
    imajina="sam",
    linkedin="",
    href="a",
    linkedin2="")



        
    