
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link353():
    getList(
        datea=None,
        getDatea=None,
numero="353",
        LA_name="Ceredigion",
        LA_pr="https://www.ceredigion.gov.uk/resident/news/",
    links="https://www.ceredigion.gov.uk/resident/news/",
    listas=".row.news-grid",
    datesss="p.small",
    replaceDate=None,
    title="h3",
    getBody=getBody,
    content=".main-content",
    imajina="sam",
    imajinasi="img.img-responsive",
    linkedin="https://www.ceredigion.gov.uk",
    href="a",
    linkedin2="https://www.ceredigion.gov.uk")


