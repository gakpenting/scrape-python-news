
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link384():
    getList(
    numero="384",
    LA_name="Haringey",
    LA_pr="haringey.gov.uk/news",
    links="https://www.haringey.gov.uk/news/feed",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content-content > div.panel-pane.pane-page-content > div > div > div > div.panel-panel.panel-content > div > div.panel-pane.pane-entity-field.pane-node-body > div > div > div > div > div",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")

