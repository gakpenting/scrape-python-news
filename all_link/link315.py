
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link315():
    getList(
        datea="div.lastupdated",
        getDatea=getDate,
numero="315",
        LA_name="Dumfries and Galloway",
        LA_pr="https://www.dumgal.gov.uk/article/15085/Latest-news",
    links="https://www.dumgal.gov.uk/article/15085/Latest-news",
    listas=".item__title",
    datesss=".item__link",
    replaceDate="Page last updated: ",
    title=".item__link",
    getBody=getBody,
    content=".a-intro, a-body",
    imajina="sam",
    linkedin="",
    href=".item__link",
    linkedin2="")


