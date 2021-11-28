# -*- encoding: utf-8 -*-

"""
@File    :   falskdemo.py    
2021/10/16 12:42     Xchen~      
"""

import json
import pymongo
from database import MongoClient
from seleniumdemo import Automation
from flask_cors import CORS  # 跨域
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)       # 防止跨域
item_ = {}


# 通过method发送post请求
@app.route('/receiver/movie', methods=['POST'])
def recive_data():
    """接收数据"""
    if request.data is not None:
        datas = json.loads(request.data)
        link = datas["url"]
        item_["url"] = link
        # print(datas["data"],type(datas["data"]))
        for item in json.loads(datas['data'])["results"]:
            item.update(item_)
            print(f"book:{item}")
        # MongoClient().insertdb(item)
        return jsonify({"status": True})
    return None


if __name__ == '__main__':
    app.run('127.0.0.1', port=80, debug=True)
