
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link185():
    getList(
    pagis=0,
    numero="185",
    LA_name="Wirral",
    LA_pr="https://wirralview.com/news",
    links="https://wirralview.com/news?page=",
    listas="div.views-row",
    datesss=".wt_headlineDate.wt_notLinkColour",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content="div[property='content:encoded']",
    imajina="figure > img",
    imajinasi="sam",
    linkedin="https://wirralview.com",
    href="a",
    linkedin2="https:")


