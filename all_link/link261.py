
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link261():
    getList(
    numero="261",
        LA_name="Rushmoor",
        LA_pr="https://www.rushmoor.gov.uk/news",
    links="https://www.rushmoor.gov.uk/index.aspx?articleid=1377",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".common.center_col_offset > *:not(#print_header):not(.issue_date):not(h1):not(a):not(.clear):not(#feedback)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
