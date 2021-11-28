# -*- encoding: utf-8 -*-

"""
@File    :   seleniumdemoProxy.py    
2021/10/17 14:44     Xchen~      
"""

import loguru
import time
import pprint
import random
import warnings
import json
# from typing import List
from changfoot import ChangeFoot
from urllib.parse import urljoin
from browsermobproxy import Server
from selenium import webdriver
from readconfig import Readconfig
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

warnings.filterwarnings("ignore", category=Warning)


class BrowsermobFramework(object):
    """代理初始化"""

    def __init__(self):
        """定义一些自动化参数"""
        self.config = Readconfig().read_selenium()
        # print(self.config.get("browsermob_path"))
        self.server = Server(self.config.get("browsermob_path"))
        self.server.start()  # 启动代理
        self.proxy = self.server.create_proxy()
        self.opt = Options()
        self.opt.add_argument(self.config.get("cerf"))
        self.opt.add_argument(self.config.get("headless"))
        self.opt.add_argument(self.config.get("proxy").format(self.proxy.proxy))
        self.browser = webdriver.Chrome(executable_path=self.config.get("executable_path"), options=self.opt)
        self.wait = WebDriverWait(self.browser, self.config.get("timeout"))

    def process_request(self, request, response):
        """请求"""
        pass

    def process_response(self, response, request):
        """返回"""
        pass

    def run(self, func, *args):
        """运行"""
        self.proxy.new_har(options={'captureContent': True,
                                    'captureHeaders': True})
        func(*args)
        result = self.proxy.har
        for item in result["log"]["entries"]:
            self.process_request(item["request"], item["response"])
            self.process_response(item["response"], item["request"])

    # def __del__(self):
    #     self.proxy.close()
    #     self.browser.close()


class Demo(BrowsermobFramework):
    loguru.logger.info("爬虫开始了...")

    def process_request(self, request, response):
        """请求"""
        # print(request)

    def process_response(self, response, request):
        """接收响应"""
        foot_dict = ChangeFoot().achieve_foot_dict()
        try:
            if '/ajax/poi/995467284567923' in request["url"]:  # 判断xhr请求链接
                # print(response["content"],type(response["content"]))
                item_ = response["content"]["text"]
                if item_ is not None:
                    # print(item_,type(item_))
                    # pprint.pprint(item_)
                    for item in json.loads(item_)["data"]["poi_info"]["discount_info"]:
                        info = item["info"]
                        print(item)
                    for num, code in foot_dict.items():
                        print(num,code)
                        # time.sleep(1)
                        # if code in info:
                        #     item["info"].replace(code, num)
                        #     print(item)
                    #         item.update(url=request["url"])
                    #         print(item)
        except Exception as e:
            loguru.logger.warning(e)

    def achieveTolpage(self):
        """获取做大页码"""
        try:
            total_page = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//ul[@class="el-pager"]/li[8]'))).text
            return total_page
        except TimeoutException as t:
            loguru.logger.error(t)

    def urlList(self):
        # for page in range(1, 11):
        #     url = urljoin(self.config.get("url"), f"/page/{str(page)}")
        yield self.config.get("url")

    def loading(self, url):
        self.browser.get(url)
        time.sleep(random.randint(2, 3))


if __name__ == '__main__':
    demo = Demo()
    for url in demo.urlList():
        demo.run(demo.loading, url)
