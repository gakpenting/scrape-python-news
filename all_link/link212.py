
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link212():
    getList(
    pagis=1,
    numero="212",
    LA_name="Mole Valley",
    LA_pr="https://news.molevalley.gov.uk/",
    links="https://news.molevalley.gov.uk/page/",
    listas=".blog-entry-inner",
    datesss="time.published",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content="div.entry-content",
    imajina="article img:not(.sfsi_wicon)",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")


