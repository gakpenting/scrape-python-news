
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import re
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link187():
    getList(
    numero="187",
    LA_name="Northamptonshire",
    LA_pr="https://www.northamptonshire.gov.uk/news/council-news/Pages/default.aspx",
    links="https://www.northamptonshire.gov.uk/news/council-news/_layouts/15/ncc.webplatform.core/handlers/NCCRSS.ashx",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField",
    imajina=".ncc-blog-details-image > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="https://www.northamptonshire.gov.uk")
