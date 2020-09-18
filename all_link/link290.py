
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link290():
    getList(
        datea=".publishedDate",
        getDatea=getDate,
numero="290",
        LA_name="Great Yarmouth",
        LA_pr="https://www.great-yarmouth.gov.uk/news",
    links="https://www.great-yarmouth.gov.uk/currentpressreleases",
    listas="#list > ul > li",
    datesss="h2",
    replaceDate=None,
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    title="h2",
    getBody=getBody,
    content="#introtext, #bodytext",
    imajina="#relatedimg0 > img",
    linkedin="",
    href="a",
    linkedin2="")


