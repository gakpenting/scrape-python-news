
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link151():
    getList(
    pagis=1,
    numero="151",
    LA_name="Tower Hamlets",
    LA_pr="https://www.towerhamlets.gov.uk/News_events/News.aspx",
    links="https://www.towerhamlets.gov.uk/News_events/News.aspx?NewsListing_List_GoToPage=",
    listas=".sys_subitem",
    datesss=".sys_subitem>div>.sys_subitem-summary>dl>dd.sys_news-datepublished",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".sys_subitem>div>h2",
    getBody=getBody,
    content=".sys_record-control>:not(div)",
    imajina=".sys_record-control>div.sys_record-image-control>img",
    imajinasi="sam",
    linkedin="https://www.towerhamlets.gov.uk",
    href=".sys_subitem>div>h2>a",
    linkedin2="https://www.towerhamlets.gov.uk")


