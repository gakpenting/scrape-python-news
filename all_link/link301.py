
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link301():
    getList(
        datea=None,
        getDatea=None,
numero="301",
        LA_name="Causeway Coast and Glens",
        LA_pr="https://www.causewaycoastandglens.gov.uk/news",
    links="https://www.causewaycoastandglens.gov.uk/news",
    listas="#news > tbody > tr",
    datesss=".news-date",
    replaceDate="Press Releases",
    title="h2",
    getBody=getBody,
    content="article > p:not(.news-date)",
    imajina=".img-news-home",
    linkedin="https://www.causewaycoastandglens.gov.uk",
    href="a",
    linkedin2="")


