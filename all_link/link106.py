
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link106():
    getList(
    numero="106",
    LA_name="Nottingham",
    LA_pr="http://www.mynottinghamnews.co.uk/main-news-page/",
    links="https://www.nottinghampost.com/?service=rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".article-body >*:not(form):not(iframe):not(script):not(div):not(aside)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

