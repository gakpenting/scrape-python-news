
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link362():
    getList(
        datea=None,
        getDatea=None,
numero="362",
        LA_name="Vale of Glamorgan",
        LA_pr="https://www.valeofglamorgan.gov.uk/en/our_council/press_and_communications/latest_news/Latest-News.aspx",
    links="https://www.valeofglamorgan.gov.uk/en/our_council/press_and_communications/latest_news/Latest-News.aspx",
    listas="#Main-Content-Container > div > div.col-12.col-md-10.col-xl-8 > div:not(#bread):not(.clear):not(.NewsListingSearch):not(.divide):not(.cleardivbread):not(:nth-child(16))",
    datesss=".NewsListingHeader",
    replaceRegex="\d{1,2}\/\d{1,2}\/\d{4}",
    title=".NewsListingHeader > a",
    getBody=getBody,
    content="#Main-Content-Container > div > div.col-12.col-md-10 > p",
    imajina="sam",
    linkedin="",
    href="a",
    linkedin2="")

