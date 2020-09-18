
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link346():
    getList(
    numero="346",
        LA_name="Newcastle upon Tyne",
        LA_pr="https://www.newcastle.gov.uk/citylife-news",
    links="https://www.newcastle.gov.uk/citylife-news/rss.xml",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="body > div.dialog-off-canvas-main-canvas > div.main-container.container.js-quickedit-main-content > div > section > div.region.region-content > div.row.bs-1col.node.node--type-general-news.node--view-mode-full > div > div.col-sm12.col-xs-12 > div.news-article-right-column > div.col-xs-12.col-sm-12.col-md-9",
    imajina=".news-img-holder > div > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.newcastle.gov.uk")
