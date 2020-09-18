
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link291():
    getList(
    numero="291",
        LA_name="King's Lynn and West Norfolk",
        LA_pr="https://www.west-norfolk.gov.uk/newsroom",
    links="https://www.west-norfolk.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".lead, .editor",
    imajina="figure > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https:")

