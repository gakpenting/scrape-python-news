import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link342():
    getList(
    numero="342",
        LA_name="Guildford",
        LA_pr="https://www.guildford.gov.uk/newsandevents",
    links="https://www.guildford.gov.uk/article/19215/News-RSS",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".textblock-default",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
