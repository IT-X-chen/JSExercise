# -*- encoding: utf-8 -*-

"""
@File    :   seleniumdemo.py    
2021/10/16 21:28     Xchen~      
"""
import warnings
import time
import random
from loguru import logger
from selenium import webdriver
from readconfig import Readconfig
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.filterwarnings("ignore", category=Warning)


class Automation(object):
    def __init__(self):
        self.config = Readconfig().read_selenium()
        self.opt = Options()
        self.opt.add_argument(self.config.get("headless"))
        self.browser = webdriver.Chrome(executable_path=self.config.get("executable_path"),options=self.opt)
        self.wait = WebDriverWait(self.browser, self.config.get("timeout"))

    def turnPage(self):
        """翻页"""
        try:
            self.browser.get(self.config.get("url"))
            self.browser.execute_script(open(self.config.get("hook_path"),encoding="utf-8").read())
            logger.info("自动化开始了....")
            time.sleep(1)
            total_page = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//ul[@class="el-pager"]/li[8]'))).text
            # self.browser.refresh()
            time.sleep(1)
            for page in range(int(total_page)):
                # if self.wait.until(EC.text_to_be_present_in_element((By.XPATH, f'//ul[@class="el-pager"]/li[{page}]'),str(page))):
                button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-next')))
                button.click()
                # self.browser.execute_script("arguments[0].click();", button)  # js翻页
                time.sleep(random.randint(2,3))
            self.browser.close()
        except TimeoutException as e:
            logger.error(e)


if __name__ == '__main__':
    Automation().turnPage()

    # #index > div:nth-child(2) > div > div > div > ul > li:nth-child(2)

