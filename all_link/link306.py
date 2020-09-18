
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link306():
    getList(
        datea=".content > p:last-child",
        getDatea=getDate,
numero="306",
        LA_name="Bassetlaw",
        LA_pr="https://www.bassetlaw.gov.uk/media-centre/news/",
    links="https://www.bassetlaw.gov.uk/media-centre/news/latest-news/",
    listas="h2",
    datesss="a",
    replaceDate="Last Updated on",
    title="a",
    getBody=getBody,
    content=".content > p:not(:last-child)",
    imajina=".news-image > img",
    linkedin="https://www.bassetlaw.gov.uk",
    href="a",
    linkedin2="https://www.bassetlaw.gov.uk")





