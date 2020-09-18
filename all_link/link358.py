
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link358():
    getList(
    numero="358",
        LA_name="Neath Port Talbot",
        LA_pr="https://www.npt.gov.uk/15639",
    links="https://www.npt.gov.uk/xml/RSSFeeds.aspx?feed=pressreleases",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#maincontent > p.lead, #maincontent > div:nth-child(5)",
    imajina="#maincontent > div:nth-child(4) > div > a > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.npt.gov.uk")
