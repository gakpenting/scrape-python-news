
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link201():
    getList(
    pagis=1,
    numero="201",
    LA_name="Na h-Eileanan Siar",
    LA_pr="https://www.cne-siar.gov.uk/news/?fl",
    links="https://www.cne-siar.gov.uk/news/?page=",
    listas=".cnes_newsitem",
    datesss="time",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content=".cnes_pagetext",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.cne-siar.gov.uk",
    href="a",
    linkedin2="")


