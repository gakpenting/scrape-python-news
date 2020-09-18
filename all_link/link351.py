
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link351():
    getList(
    numero="351",
        LA_name="Cardiff",
        LA_pr="https://www.cardiff.gov.uk/ENG/Your-Council/News/Pages/default.aspx",
    links="https://www.cardiffnewsroom.co.uk/rss_cardiff.xml",
    listas="item",
    datesss="pubdate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".MsoNormal",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

