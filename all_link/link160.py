
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link160():
    getList(
    pagis=1,
    numero="160",
    LA_name="Dacorum",
    LA_pr="https://www.dacorum.gov.uk/home/news",
    links="https://www.dacorum.gov.uk/home/news/page/",
    listas="ul.news_list > li",
    datesss="a > span.text > span:nth-child(2)",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".h3",
    getBody=getBody,
    content=".sfnewsContent > p",
    imajina="sam",
    imajinasi=".content > img",
    linkedin="https://www.dacorum.gov.uk",
    href="a",
    linkedin2="")


