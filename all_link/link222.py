import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link222():
    getList(
    numero="222",
    LA_name="West Berkshire",
    LA_pr="https://info.westberks.gov.uk/news",
    links="https://info.westberks.gov.uk/news",
    listas="#newsnewsitems > * > *",
    datesss="span.timedate",
    replaceDate=None,
    title="a",
    getBody=getBody,
    content="#defaultcontent > *:not(h1)",
    imajina=".rimage > img",
    linkedin="",
    href="a",
    linkedin2="")

