
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link410():
    getList(
    numero="410",
    LA_name="Ryedale",
    LA_pr="ryedale.gov.uk/your-council/news",
    links="https://news.ryedale.gov.uk/feed/rss",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".content-summary, .content-body",
    imajina="body > main > div > div.c-width-large-3-4 > div > div.hero-image.margin-xlarge-bottom > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

