# -*- encoding: utf-8 -*-

"""
@File    :   V8运行.py    
2021/11/16 22:31     Xchen~      
"""
import PyV8  # 注意大小写
with open('完美世界-pwd-rsa.js',mode="r",encoding="utf-8") as fp:
    text = fp.read()
with PyV8.JSContext() as ctx:
    ctx.eval(text)
res = ctx.locals.getpwd("123456")
print(res)
# import sys
# print(sys.path)