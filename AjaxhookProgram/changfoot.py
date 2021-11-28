# -*- encoding: utf-8 -*-

"""
@File    :   changfoot.py    
2021/10/18 18:34     Xchen~      
"""

import requests
import random
import time
import base64
from fontTools.ttLib import TTFont
from io import BytesIO
class ChangeFoot(object):
    def __init__(self):
        self.font = "https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/2dd8f5f0.woff"
        self.map = {}  # 组成映射关系
        self.new_map={}  # 最终字体字典
        self.nums = ['.', 6, 5, 3, 9, 8, 7, 1, 4, 2, 0]

    # def handler_request(self,url):
    #     """请求方法"""
    #     try:
    #         response = requests.get(self.url)
    #         if response.status_code == requests.codes.ok:
    #             response.encoding = response.apparent_encoding
    #             return response.content.decode("utf-8")
    #         return None
    #     except requests.exceptions as e:
    #         logger.error(e)

    def achieve_foot_dict(self):
        html_str = self.handler_request(url)
        font_url = "https:" + re.compile(r",url\(\"(.*woff)\"\)").search(html_str).group(1)
        with open("f.woff", mode="wb") as fp:
            fp.write(requests.get(font_url).content)
            time.sleep(random.randint(1, 2))
        font = TTFont("1.woff")
        font.saveXML("1.xml")
        for code,name in font['cmap'].getBestCmap().items():
            code = str(hex(code)).replace('0', '&#', 1) + ';'
            self.map[name] = code  # 组成映射关系
        for id,num in zip(font.glyphOrder[1:],self.nums):
            self.new_map[num] = self.map[id]
        # print(self.new_map)
        return self.new_map


# ChangeFoot().achieve_foot_dict()