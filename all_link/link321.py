
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link321():
    getList(
        datea=".pagelastupdated",
        getDatea=getDate,
numero="321",
        LA_name="North Lanarkshire",
        LA_pr="https://www.northlanarkshire.gov.uk/index.aspx?articleid=12455",
    links="https://www.northlanarkshire.gov.uk/index.aspx?articleid=12455",
    listas="#list > ul > li",
    datesss="h2",
    replaceRegex="\d{1,2}\s\w+\s\d{4}",
    title="h2",
    getBody=getBody,
    content="#bodytext, #introtext",
    imajina=".image > img",
    linkedin="",
    href="a",
    linkedin2="")



