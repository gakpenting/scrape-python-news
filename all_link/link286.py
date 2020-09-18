
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link286():
    getList(
    numero="286",
        LA_name="Knowsley",
        LA_pr="https://www.knowsleynews.co.uk/",
    links="https://www.knowsleynews.co.uk/feed/",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#penci-post-entry-inner",
    imajina=".post-image > a > img, #penci-post-entry-inner > p > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")
