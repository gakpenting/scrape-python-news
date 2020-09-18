
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link205():
    getList(
        datea=None,
        getDatea=None,
numero="205",
    LA_name="Somerset",
    LA_pr="https://somersetnewsroom.com/",
    links="https://somersetnewsroom.com/",
    listas="#hfeed > div",
    datesss=".published",
    replaceDate=None,
    title="h2",
    getBody=getBody,
    content=".entry-content > p",
    imajina="figure > img",
    linkedin="",
    href="a",
    linkedin2="")

