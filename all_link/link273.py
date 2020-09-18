
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link273():
    getList(
    numero="273",
        LA_name="Chorley",
        LA_pr="https://choosechorley.co.uk/news/Pages/default.aspx",
    links="https://chorleybusinesssupport.co.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".entry-content",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")


