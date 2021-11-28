'''
i: 狗
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16136300015509
sign: e355389c25a95b4a5b0dcbb7e95e897f
lts: 1613630001550
bv: 3da01a09873456cfb5dba05f2124b148
doctype: json
version: 2.1.html
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION

'''

import random
import time
from hashlib import md5

def get(word):
    time_data=int(time.time()*1000)
    ts=str(time_data)
    salt=ts+str(random.randint(0,9))
    # sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
    sign_str="fanyideskweb"+word+salt+"Tbh5E8=q6U3EXe+&L[4c@"
    md=md5()
    # encode(encoding='UTF-8')
    # md.update(b'%s'%sign_str)
    md.update(sign_str.encode())
    sign=md.hexdigest()
    print(ts,salt,sign)



get('我喜欢你')




'''
>>> hashlib.md5('你好'.encode(encoding='UTF-8')).hexdigest()
'7eca689f0d3389d9dea66ae112e5cfd7'
 
>>> hashlib.md5('你好'.encode(encoding='GBK')).hexdigest()
'b94ae3c6d892b29cf48d9bea819b27b9'
 
>>> hashlib.md5('你好'.encode(encoding='GB2312')).hexdigest()
'b94ae3c6d892b29cf48d9bea819b27b9'
 
>>> hashlib.md5('你好'.encode(encoding='GB18030')).hexdigest()
'b94ae3c6d892b29cf48d9bea819b27b9'


>>> import hashlib
>>> m = hashlib.md5()
>>> m.update(b'123')
>>> m.hexdigest()
'202cb962ac59075b964b07152d234b70'
 
# 或者可以这样（最常见的写法，常用于图片的命名）
>>> hashlib.md5(b'123').hexdigest()
'202cb962ac59075b964b07152d234b70'
 
# 也可以使用hash.new()这个一般方法，hashlib.new(name[, data])，name传入的是哈希加密算法的名称，如md5
>>> hashlib.new('md5', b'123').hexdigest()
'202cb962ac59075b964b07152d234b70'
以上是对于英文进行md5加密的，如果要对中文进行加密，发现按照上面来写会报错，原因在于字符转码问题，要如下写：

1.html
2
3
4
>>> import hashlib
>>> data = '你好'
>>> hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
'7eca689f0d3389d9dea66ae112e5cfd7'


'''
