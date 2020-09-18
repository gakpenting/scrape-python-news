
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link137():
    getList(
    numero="137",
    LA_name="Worcestershire",
    LA_pr="http://www.worcestershire.gov.uk/news_social_media",
    links="http://www.worcestershire.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".main-content>article>*:not(img):not(:last-child):not(span)",
    imajina=".main-content>article>img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

