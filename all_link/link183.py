
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link183():
    getList(
    pagis=1,
    numero="183",
    LA_name="West Lindsey",
    LA_pr="https://www.west-lindsey.gov.uk/my-council/council-news/",
    links="https://www.west-lindsey.gov.uk/my-council/council-news/?lister10319p=",
    listas="#-ux-content > div > div > div > div.column-outer.column-alpha > div > div > div.oBoxContainer.oHeadlineBoxStyle1.pel.lister.lister-list.style-1.show-images > div.oBoxOuter.oPageListerContainerOuter.pel-o > div > div > div > ul > li",
    datesss="#-ux-content > div > div > div > div.column-outer.column-alpha > div > div > div.oBoxContainer.oHeadlineBoxStyle1.pel.lister.lister-list.style-1.show-images > div.oBoxOuter.oPageListerContainerOuter.pel-o > div > div > div > ul > li > span > span.oBoxItemOuter.item-body-outer > span > span.oBoxItemDate.item-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="#-ux-content > div > div > div > div.column-outer.column-alpha > div > div > div.oBoxContainer.oHeadlineBoxStyle1.pel.lister.lister-list.style-1.show-images > div.oBoxOuter.oPageListerContainerOuter.pel-o > div > div > div > ul > li> span > span.oBoxItemOuter.item-body-outer > span > span.oBoxItemTitle.item-title > a",
    getBody=getBody,
    content="#-ux-content > div > div > div > div.column-outer.column-alpha > div > div > div.contenteditor:not(:first-child)",
    imajina="#espr_renderHost_PageStructureDisplayRenderer_esctl_06469bbf-4978-4720-89e5-0566e4280f3f_InnerRenderer_06469bbf-4978-4720-89e5-0566e4280f3f_esctl_ffdf455f-7c7e-460d-bde1-e0576e7fba74_InnerRenderer_ffdf455f-7c7e-460d-bde1-e0576e7fba74_esctl_fe78f664-c737-4bb2-ba68-0d7f99c635f3_pnlAssetImgHolder > div > img",
    imajinasi="sam",
    linkedin="https://www.west-lindsey.gov.uk",
    href="#-ux-content > div > div > div > div.column-outer.column-alpha > div > div > div.oBoxContainer.oHeadlineBoxStyle1.pel.lister.lister-list.style-1.show-images > div.oBoxOuter.oPageListerContainerOuter.pel-o > div > div > div > ul > li> span > span.oBoxItemOuter.item-body-outer > span > span.oBoxItemTitle.item-title > a",
    linkedin2="https://www.west-lindsey.gov.uk")


