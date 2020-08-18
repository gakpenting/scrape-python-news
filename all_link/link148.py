
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link148():
    getList(
    pagis=1,
    numero="148",
    LA_name="Islington",
    LA_pr="https://www.islington.media/news",
    links="https://www.islington.media/news?page=",
    listas=".cell.cell-contained.no-padding",
    datesss=".cell.cell-contained.no-padding>div.flex>p.date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".cell.cell-contained.no-padding>div.flex>h3",
    getBody=getBody,
    content=".content-body>*",
    imajina="sam",
    imajinasi=".cell.cell-contained.no-padding>.thumbnail>a>img",
    linkedin="https://www.islington.media",
    href=".cell.cell-contained.no-padding>.thumbnail>a",
    linkedin2="")


