
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link141():
    getList(
    pagis=1, 
    numero="141",
    LA_name="Isles of Scilly",
    LA_pr="https://www.scilly.gov.uk/most-recent-news-items",
    links="https://www.scilly.gov.uk/most-recent-news-items?page=", # iki genti
    listas="#block-system-main > div > div > div.view-content > div.views-row", # iki genti
    datesss=None, #iki genti
    replaceDate="Publishing date: ", # lek misal ono publishing date
    replaceRegex=None,
    datea=".date-display-single", # lek misal gaono date ndek depan
    getDatea=getDate, # lek misal gaono date ndek depan
    title="span.field-content", # title awal
    getBody=getBody,
    content="div[property='content:encoded']",# ganti
    imajina="sam", # misal ada gambar di content
    imajinasi="sam", # misal ada gambar di depan
    linkedin="", # link
    href="a",
    linkedin2="" # link
    )


