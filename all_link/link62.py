import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link62():
    getList(        
    numero="62",
    LA_name="Braintree",
    LA_pr="https://www.braintree.gov.uk/news",
    links="https://www.braintree.gov.uk/news",
    listas="li.article-listing__article",
    datesss="small.article-listing__article-date",
    replaceDate="Published: ",
    getDatea=None,
    title="h2",
    content=".editor",
    imajina="sam",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")
