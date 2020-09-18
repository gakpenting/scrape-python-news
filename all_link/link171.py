
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link171():
    getList(
    pagis=1,
    numero="171",
    LA_name="Tonbridge and Malling",
    LA_pr="https://www.tmbc.gov.uk/news",
    links="https://www.tmbc.gov.uk/news?result_9913_result_page=",
    listas=".article-mainbody>ul>li",
    datesss=".article-mainbody>ul>li > p:nth-child(3)",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title=".article-mainbody>ul>li> h2",
    getBody=getBody,
    content=".article-mainbody >div>div.desc>*",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href=".article-mainbody>ul>li > p:nth-child(2)>a",
    linkedin2="https://www.tmbc.gov.uk")


