
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link323():
    getList(
        datea=".last-modified-date",
        getDatea=getDate,
numero="323",
        LA_name="Perth and Kinross",
        LA_pr="https://www.pkc.gov.uk/news",
    links="https://www.pkc.gov.uk/news",
    listas=".grid__cellwrap",
    datesss="h2",
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    title="h2",
    getBody=getBody,
    content=".textblock-default",
    imajina="sam",
    linkedin="",
    href="a",
    linkedin2="")

