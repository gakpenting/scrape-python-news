
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link169():
    getList(
    pagis=1,
    numero="169",
    LA_name="Folkestone and Hythe",
    LA_pr="https://www.folkestone-hythe.gov.uk/article/30/News",
    links="https://www.folkestone-hythe.gov.uk/news?p=",
    listas=".item.item--article",
    datesss="div",
    replaceDate=None,
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    getDatea=getDate,
    datea="#maincontent > div.container > div > div.a-body.a-body--default > p:last-child",
    title=".item__link",
    getBody=getBody,
    content=".a-body.a-body--default",
    imajina=".a-relimage.a-relimage--default > img",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")


