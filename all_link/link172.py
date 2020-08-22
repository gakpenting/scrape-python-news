
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link172():
    getList(
    pagis=1,
    numero="172",
    LA_name="Blackpool",
    LA_pr="https://www.blackpool.gov.uk/News/News.aspx",
    links="https://www.blackpool.gov.uk/News/News.aspx?Archive_Listing_List_GoToPage=",
    listas="#Archive_Listing_List>*>div.sys_subitem",
    datesss="#Archive_Listing_List>*>div.sys_subitem > div > div.sys_subitem-summary>dl>dd.sys_news-datepublished",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="#Archive_Listing_List>*>div.sys_subitem > div > h2",
    getBody=getBody,
    content=".sys_record-control.sys_news-record>*:not(table):not(div)",
    imajina=".sys_record-control.sys_news-record>div.sys_record-image-control>img",
    imajinasi="sam",
    linkedin="https://www.blackpool.gov.uk",
    href="#Archive_Listing_List>*>div.sys_subitem > div > h2>a",
    linkedin2="https://www.blackpool.gov.uk")


