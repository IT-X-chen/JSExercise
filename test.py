# # -*- encoding: utf-8 -*-
#
# """
# @File    :   test.py
# 2021/10/30 14:53     Xchen~
# """
# import sys
# import os
# import execjs
# import subprocess
#
# # os.environ["EXECJS_RUNTIME"] = "JScript"
# # with open("天翼云-password-webpack.js",mode="r",encoding="utf-8") as fp:
# #     text = fp.read()
# # # text=text.replace(u'\xa0\xa9', u'')
# # js = execjs.compile(text)
# # v = js.call("get","123456")
# # print(v)
#
# # import os
# # # https://www.jianshu.com/p/430c411160f8
# # # pipline = os.system("node ./天翼云-password-webpack.js")
# # # p = os.popen("node ./天翼云-password-webpack.js","")
# a = subprocess.getstatusoutput("node ./天翼云-password-webpack.js")[-1]
# print(a)
#
#
#
#
# import subprocess
# p = subprocess.Popen("node ./天翼云-password-webpack.js",
#                      shell=True,
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.STDOUT,
#                      encoding='utf-8'
#                      )
#
# # 输出stdout
# print(p.communicate()[0])


import re
from loguru import logger

print(f"{'*' * 50}原油计算小程序{'*' * 50}")


# # 1.让用户输入 最大和 最小数
# from random import randint
# # import random
# max_num = int(input('来了老弟, 请你输入要猜的最大数字吧'))
# min_num = int(input('来了老弟, 请你输入要猜的最小数字吧'))
# # 2. 生成[min_num, max_num] 的一个随机数
# generate_num = randint(min_num, max_num)
# # random.randint(min_num, max_num)
# # 3. 声明一个猜数字次数的变量,并进入循环
# count = 0
# while True:



while True:
    oil_price = int(input('请输入原油价格:'))
    oil_lit = input('请输入原油数量:')
    if re.search('\D',oil_lit):
        price = oil_price * int(re.search("^\d+",oil_lit).group())
        print(f"原油总价格为:{price:.2f}元")
    else:
        print("输入错误请从新输入！！！")
        continue
    conditions = input("还继续吗:[y|Y]:")
    if conditions in ["y","Y"]:
        continue
    else:
        print("欢迎下次光临！！！")
        break

