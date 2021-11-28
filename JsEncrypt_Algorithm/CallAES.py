# -*- encoding: utf-8 -*-

"""
@File    :   CallAES.py    
2021/10/13 16:36     Xchen~      
"""
import execjs


def achieveSecretkey(word):
    """获得加密密码"""
    with open('../JS/AES.js', mode="r", encoding="utf-8") as fp:
        text = fp.read()
    key = execjs.compile(text)
    print(f"加密前:{word}")
    result = key.call("AES_Encrypt", word)
    return result


if __name__ == '__main__':
    res = achieveSecretkey("123456")
    print(f"加密后:{res}")
