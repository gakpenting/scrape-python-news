
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link105():
    getList(
    pagis=1,
    numero="105",
    LA_name="Newry, Mourne and Down",
    LA_pr="https://www.newrymournedown.org/news",
    links="https://www.newrymournedown.org/news/",
    listas="#maincontent > div.cell_full > div.cell_full_sub > div.list_date > ul > li",
    datesss=".card-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h4",
    getBody=getBody,
    content=".section_date_content_detail > p",
    imajina="#maincontent > div.cell_full > div.cell_full_sub > section > div.section_date_content_img > div.my-simple-gallery > figure > a > img",
    imajinasi="sam",
    linkedin="",
    href="a",
    linkedin2="")


