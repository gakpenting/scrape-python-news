
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link181():
    getList(
    pagis=1,
    numero="181",
    LA_name="North Kesteven",
    LA_pr="https://www.n-kesteven.gov.uk/your-council/council-news/",
    links="https://www.n-kesteven.gov.uk/your-council/news/council-news/?lister12074p=",
    listas="#-ux-content > div > div > div > div.column-outer.column-alpha > div > div > div.oBoxContainer.oHeadlineBoxStyle1.pel.lister.lister-list.style-1.show-images > div.oBoxOuter.oPageListerContainerOuter.pel-o > div > div > div > ul > li",
    datesss="span > span.oBoxItemOuter.item-body-outer > span > span.oBoxItemDate.item-date",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="span > span.oBoxItemOuter.item-body-outer > span > span.oBoxItemTitle.item-title > a",
    getBody=getBody,
    content="#-ux-content > div > div > div > div.column-outer.column-alpha > div > div > div>*:not(div):not(span)",
    imajina="#espr_renderHost_PageStructureDisplayRenderer_esctl_7ccbe766-b5cc-4f77-b1ad-1585c8ccc003_InnerRenderer_7ccbe766-b5cc-4f77-b1ad-1585c8ccc003_esctl_6aef6f7c-a901-4f51-b56d-e0d8d49c4378_InnerRenderer_6aef6f7c-a901-4f51-b56d-e0d8d49c4378_esctl_8a74af61-dc0f-4ded-a490-063e6178bd43_pnlAssetImgHolder > div > img",
    imajinasi="sam",
    linkedin="https://www.n-kesteven.gov.uk",
    href="span > span.oBoxItemOuter.item-body-outer > span > span.oBoxItemTitle.item-title > a",
    linkedin2="https://www.n-kesteven.gov.uk")


