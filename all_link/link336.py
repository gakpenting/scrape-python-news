
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link336():
    getList(
        datea="#default > div.maincontent > div > div.maincontent__left > div.maincontent__bodytext > p:nth-child(1)",
        getDatea=getDate,
numero="336",
        LA_name="Staffordshire Moorlands",
        LA_pr="https://www.staffsmoorlands.gov.uk/article/416/News--Events",
    links="https://www.staffsmoorlands.gov.uk/article/416/News--Events",
    listas="#listv2 > div.maincontent > div > div > div.grid.grid--list.grid--2col > div:nth-child(1) > div > div > ol > li",
    datesss="a",
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    title=".tabcontent__link.list__childlink",
    getBody=getBody,
    content=".maincontent__bodytext > p:not(:first-child)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")

