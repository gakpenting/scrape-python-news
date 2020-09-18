
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.page.nopages import getList
from all_link.helpers.helper import getDate,getBody
def link375():
    getList(
        datea="#ctl00_PlaceHolderMain_NewsroomByline_output",
        getDatea=getDate,
numero="375",
        LA_name="Wakefield",
        LA_pr="https://www.wakefield.gov.uk/about-the-council/newsroom",
    links="https://www.wakefield.gov.uk/about-the-council/newsroom",
    listas=".nr-home-latest",
    datesss="div",
    replaceRegex="\d{1,2}\/\d{1,2}\/\d{4}",
    title=".nr-home-text > strong",
    getBody=getBody,
    content="#ctl00_PlaceHolderMain_PageContent1__ControlWrapper_RichHtmlField > p,#ctl00_PlaceHolderMain_PageContent2__ControlWrapper_RichHtmlField > p",
    imajina="#ctl00_PlaceHolderMain_nraImage0 > img",
    linkedin="https://www.wakefield.gov.uk",
    href="a",
    linkedin2="https://www.wakefield.gov.uk")
