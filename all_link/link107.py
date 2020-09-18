
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link107():
    getList(
        datea="#contentArea > p:nth-child(2)",
        getDatea=getDate,
numero="107",
    LA_name="Rushcliffe",
    LA_pr="https://www.rushcliffe.gov.uk/aboutus/newsandpublications/latestnews/",
    links="https://www.rushcliffe.gov.uk/aboutus/newsandpublications/latestnews/",
    listas="#contentArea > h2",
    datesss="a",
    replaceDate=None,
    title="a",
    getBody=getBody,
    content="#contentArea > p:not(:nth-child(2))",
    imajina="#contentArea > p:nth-child(4) > img",
    imajinasi="sam",
    linkedin="https://www.rushcliffe.gov.uk",
    href="a",
    linkedin2="https://www.rushcliffe.gov.uk")
