
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link155():
    getList(
    pagis=1,
    numero="155",
    LA_name="Trafford",
    LA_pr="https://www.trafford.gov.uk/residents/news/news-archive.aspx",
    links="https://www.trafford.gov.uk/residents/news/news-archive.aspx?Archive_Listing_List_GoToPage=",
    listas=".sys_subitem",
    datesss=".sys_subitem>div>.sys_subitem-summary>dl>dd.sys_news-datepublished",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".sys_subitem>div>h3",
    getBody=getBody,
    content="#main-article>div.sys_none>div>*:not(div)",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.trafford.gov.uk",
    href=".sys_subitem>div>h3>a",
    linkedin2="https://www.trafford.gov.uk")


