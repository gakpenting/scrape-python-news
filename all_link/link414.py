
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link414():
    getList(
        datea=None,
        getDatea=None,
numero="414",
LA_name="South Ayrshire",
LA_pr="south-ayrshire.gov.uk/news",
    links="https://www.south-ayrshire.gov.uk/news/",
    listas="#contentPanel_newspanel > div",
    datesss="a > div.col-sm-7 > p:nth-child(3)",
    replaceDate=None,
    title="h2",
    getBody=getBody,
    content=".news-text",
    imajina="#contentPanel_theimage > img",
    linkedin="https://www.south-ayrshire.gov.uk",
    href="a",
    linkedin2="",
    dayfirst=False
    )


