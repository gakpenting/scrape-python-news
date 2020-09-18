
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link104():
    getList(
    numero="104",
    LA_name="Northern Ireland",
    LA_pr="https://www.northernireland.gov.uk/press-releases",
    links="https://www.northernireland.gov.uk/press-releases/rss.xml",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".pane-content.tighten",
    imajina="#contentTypeNews > div.panel-panel.main > div > div > div > picture > img",
    imajinasi="sam",
    linkedin="",
    href="guid",
    linkedin2="")

