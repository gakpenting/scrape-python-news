
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link355():
    getList(
        datea=None,
        getDatea=None,
numero="355",
        LA_name="Flintshire",
        LA_pr="https://www.flintshire.gov.uk/en/Resident/Council-Apps/News-Archive.aspx",
    links="https://www.flintshire.gov.uk/en/Resident/Council-Apps/News-Archive.aspx",
    listas="#form1 > section > div > div.col-md-8.page-content > ul > li",
    datesss="span.label.label-primary.label-pill.pull-right",
    replaceDate=None,
    title="a",
    getBody=getBody,
    content=".page-content > p",
    imajina=".page-content > p > a > img",
    linkedin="https://www.flintshire.gov.uk",
    href="a",
    linkedin2="")

