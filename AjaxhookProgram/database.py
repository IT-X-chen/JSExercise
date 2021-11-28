# -*- encoding: utf-8 -*-

"""
@File    :   database.py    
2021/10/16 21:01     Xchen~      
"""
import pymongo
from loguru import logger

class MongoClient(object):
    """把数据保存到mongodb数据库"""

    def __init__(self):
        self.config = Readconfig().read()

    @logger.catch()
    def connectDB(self):
        """连接数据库"""
        self.client = pymongo.MongoClient(host=self.config["host"], port=int(self.config["port"]))
        self.col = self.client[self.config.get("xchen")][self.config.get("book")]

    @logger.catch()
    def insertdb(self, item):
        self.col.insert(item)
