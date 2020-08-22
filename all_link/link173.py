
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link173():
    getList(
    pagis=1,
    numero="173",
    LA_name="Hyndburn",
    LA_pr="https://www.hyndburnbc.gov.uk/hyndburnnews/",
    links="https://www.hyndburnbc.gov.uk/hyndburnnews/page/",
    listas="article > section > div > div > div > div > div.sp_news_static.design-17.wpnaw-grid-3.wpnaw-news-grid.wpnaw-clearfix > div > div > div.news-overlay > div.news-short-content",
    datesss="article > section > div > div > div > div > div.sp_news_static.design-17.wpnaw-grid-3.wpnaw-news-grid.wpnaw-clearfix > div > div > div.news-overlay > div.news-short-content > div.news-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="article > section > div > div > div > div > div.sp_news_static.design-17.wpnaw-grid-3.wpnaw-news-grid.wpnaw-clearfix > div > div > div.news-overlay > div.news-short-content >h2",
    getBody=getBody,
    content="div.content > article > section.post_content > div > div > div > div > div>div>*",
    imajina="sam",
    imajinasi="article > section > div > div > div > div > div.sp_news_static.design-17.wpnaw-grid-3.wpnaw-news-grid.wpnaw-clearfix > div > div > div.news-overlay > div.news-image-bg>a>img",
    linkedin="",
    href="article > section > div > div > div > div > div.sp_news_static.design-17.wpnaw-grid-3.wpnaw-news-grid.wpnaw-clearfix > div > div > div.news-overlay > div.news-short-content >h2>a",
    linkedin2="")


