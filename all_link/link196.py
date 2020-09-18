
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link196():
    getList(
    pagis=0,
    numero="196",
    LA_name="Vale of White Horse",
    LA_pr="http://www.whitehorsedc.gov.uk/news",
    links="http://www.whitehorsedc.gov.uk/news?page=",
    listas="li.views-row",
    datesss=".meta",
    replaceDate=None,
    replaceRegex="\w+\s\d{1,2},\s\d{4}",
    getDatea=None,
    title="h2",
    getBody=getBody,
    content=".wys",
    imajina="sam",
    imajinasi="sam",
    linkedin="http://www.whitehorsedc.gov.uk",
    href="a",
    linkedin2="")


