
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link162():
    getList(
    pagis=1,
    numero="162",
    LA_name="Hertsmere",
    LA_pr="https://www.hertsmere.gov.uk/News/NewsHome.aspx",
    links="https://www.hertsmere.gov.uk/News/NewsHome.aspx?Listing_List_GoToPage=",
    listas=".sys_itemslist>div",
    # datesss=".sys_itemslist>div>div>div.sys_subitem-summary.sys_news-summary>dl>dd.sys_news-datepublished",
     datesss=None,
    replaceDate="Posted on ",
    replaceRegex=None,
    datea=".sys_articleContent>div>div>div.sys_news-posted-date",
    getDatea=getDate,
    title=".sys_itemslist>div>div>h3.sys_subitem-heading.sys_news-subheading",
    getBody=getBody,
    content=".sys_articleContent>div>div>*:not(.sys_news-posted-date)",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.hertsmere.gov.uk",
    href=".sys_itemslist>div>div>h3.sys_subitem-heading.sys_news-subheading>a",
    linkedin2="")


