
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link334():
    getList(
        datea="div[property='content:encoded'] > p:last-child",
        getDatea=getDate,
numero="334",
        LA_name="Newcastle-under-Lyme",
        LA_pr="https://www.newcastle-staffs.gov.uk/news",
    links="https://www.newcastle-staffs.gov.uk/news",
    listas=".view-content > .news-article",
    datesss="div",
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    title="h3",
    getBody=getBody,
    content="div[property='content:encoded'] > p:not(:last-child)",
    imajina=".img-responsive",
    imajinasi="sam",
    linkedin="https://www.newcastle-staffs.gov.uk",
    href="a",
    linkedin2="")

