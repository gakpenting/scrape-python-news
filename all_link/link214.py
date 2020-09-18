
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link214():
    getList(
        
    pagis=1,
    numero="214",
    LA_name="Conwy",
    LA_pr="https://www.conwy.gov.uk/en/Spotlight/Press-Releases/Press-Releases.aspx",
    links="https://www.conwy.gov.uk/en/Spotlight/Press-Releases/Press-Releases.aspx?Listing_List_GoToPage=",
    listas=".sys_itemslist",
    datesss=None,
    replaceDate="Posted on ",
    replaceRegex=None,
    datea=".sys_news-posted-date",
    getDatea=getDate,
    title="h2",
    getBody=getBody,
    content=".sys_record-control > *:not(h2)",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.conwy.gov.uk",
    href="a",
    linkedin2="")


