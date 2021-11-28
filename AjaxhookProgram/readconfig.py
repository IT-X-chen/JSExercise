# -*- encoding: utf-8 -*-

"""
@File    :   readconfig.py    
2021/10/16 21:50     Xchen~      
"""
import configparser

class Readconfig(object):
    def __init__(self):
        self.con = configparser.ConfigParser()
        config = self.con.read('./config.ini', encoding="utf8")

    def read_mongo(self):
        """读取mongodb配置"""
        return dict(self.con.items("mongodb"))

    def read_selenium(self):
        """读取selenium配置"""
        return dict(self.con.items("selenium"))


