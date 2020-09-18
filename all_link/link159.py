
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link159():
    getList(
    pagis=1,
    numero="159",
    LA_name="Broxbourne",
    LA_pr="https://www.broxbourne.gov.uk/news",
    links="https://www.broxbourne.gov.uk/news?page=",
    listas=".page-content>ul.list.list--listing>*",
    datesss=".page-content>ul.list.list--listing>li.list__item>article>a>div>div.listing__meta>*",
    replaceDate="Published:",
    replaceRegex=None,
    getDatea=None,
    title=".page-content>ul.list.list--listing>li.list__item>article>a>div>h2",
    getBody=getBody,
    content=".page-content>div.editor>*",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.broxbourne.gov.uk",
    href=".page-content>ul.list.list--listing>li.list__item>article>a",
    linkedin2="https://www.broxbourne.gov.uk")


