
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link186():
    getList(
    pagis=0,
    numero="186",
    LA_name="South Norfolk",
    LA_pr="https://www.south-norfolk.gov.uk/about-us/press-releases",
    links="https://www.south-norfolk.gov.uk/about-us/press-releases?page=",
    listas=".listing > .media",
    datesss=".views-field.views-field-created",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".listing__title",
    getBody=getBody,
    content=".node-content--news_article.node-content",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.south-norfolk.gov.uk",
    href="a",
    linkedin2="")


