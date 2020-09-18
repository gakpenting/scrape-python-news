
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link154():
    getList(
        datea=None,
        getDatea=None,
numero="154",
    LA_name="Bury",
    LA_pr="http://www.mynewsdesk.com/uk/bury-council/latest_news",
    links="http://www.mynewsdesk.com/uk/bury-council/latest_news",
    listas=".article.news",
    datesss=".material-date",
    replaceDate=None,
    title="h2",
    getBody=getBody,
    content=".newsroom-article",
    imajina="noscript > img",
    linkedin="http://www.mynewsdesk.com",
    href="a",
    linkedin2="")

