# -*- encoding: utf-8 -*-

"""
@File    :   demo.py    
2021/10/18 17:17     Xchen~      
"""
import requests
import re
import os
import time
import random
from loguru import logger
from fontTools.ttLib import TTFont
from os import makedirs
from os.path import exists

# resposne = requests.get('https://i.waimai.meituan.com/external/poi/995467284567923')

# RESULTS_DIR = 'fonts'
# exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def handler_request(url):
    """请求方法"""
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            response.encoding = response.apparent_encoding
            return response.content.decode("utf-8")
        return None
    except requests.exceptions as e:
        logger.error(e)


def save_file(html_str: str):
    font_url = "https:" + re.compile(r",url\(\"(.*woff)\"\)").search(html_str).group(1)
    with open("f.woff", mode="wb") as fp:
        fp.write(requests.get(font_url).content)
        time.sleep(random.randint(1,2))
    font = TTFont("f.woff")
    font.saveXML("f.xml")


html_str = handler_request('https://i.waimai.meituan.com/external/poi/995467284567923')
save_file(html_str)
