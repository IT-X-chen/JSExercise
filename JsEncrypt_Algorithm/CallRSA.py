# -*- encoding: utf-8 -*-

"""
@File    :   CallRSA.py    
2021/10/13 22:49     Xchen~      
"""

import execjs


def achievePass(password):
    """获取加密密码"""
    with open('../JS/RSA.js', mode="r", encoding="utf-8") as fp:
        text = fp.read()
    text= text.replace(u'\xa0', u'')
    # text = text.encode("gbk", 'ignore').decode("gbk", "ignore")
    data = execjs.compile(text)
    res = data.call("achieveKey", password)
    return res


if __name__ == '__main__':
    passwd = "123456789"
    res = achievePass(passwd)
    print(f"解密前:{passwd}\n解密后:{res}")
