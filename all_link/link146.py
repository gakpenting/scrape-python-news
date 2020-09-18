
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link146():
    getList(
    pagis=1,
    numero="146",
    LA_name="Harrow",
    LA_pr="https://www.harrow.gov.uk/news",
    links="https://www.harrow.gov.uk/news?page=",
    listas=".list__item>article",
    datesss=".meta.meta--date",
    replaceDate="Published: ",
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content=".page-content>p.summary,div.editor>*",
    imajina="sam",
    imajinasi="a>img",
    linkedin="https://www.harrow.gov.uk",
    href="a",
    linkedin2="https://www.harrow.gov.uk")


