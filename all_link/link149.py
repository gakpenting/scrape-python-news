
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link149():
    getList(
    pagis=1,
    numero="149",
    LA_name="Lambeth",
    LA_pr="https://love.lambeth.gov.uk/all-posts/",
    links="https://love.lambeth.gov.uk/all-posts/page/",
    listas=".more_posts",
    datesss=None,
    replaceDate="Publishing date: ", # lek misal ono publishing date
    replaceRegex=None,
    datea=".main_content>.meta>.date",
    getDatea=getDate,
    title=".more_posts>*>.more_post_text>h4",
    getBody=getBody,
    content=".post_text>*",
    imajina="sam",
    imajinasi=".more_posts>*>.promobox>img",
    linkedin="",
    href=".more_posts>a",
    linkedin2="")


