import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link63():
    getList(        
    numero="63",
    LA_name="Brentwood",
    LA_pr="http://www.brentwood.gov.uk/index.php?cid=826",
    links="http://www.brentwood.gov.uk/index.php?cid=826",
    listas="div#content > :nth-child(7) > li",
    datesss="a",
    replaceRegexTitle=r"\d{1,2}\s\w+\s\d{4,}\,",
    replaceDate=None,
    getDatea=None,
    title="a",
    content="div.span9 > p:not(:nth-of-type(1))",
    imajina="sam",
    getBody=getBody,
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")
