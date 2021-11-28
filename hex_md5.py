# -*- encoding: utf-8 -*-

"""
@File    :   hex_md5.py    
2021/11/16 16:43     Xchen~      
"""

from hashlib import md5

key = "s^H8"
pwd = "123456"
data = pwd + key
data_ = md5(data.encode('utf-8')).hexdigest()
# a = data_.upper()[0:5]
res = md5(str(data_.upper()[:5]+data_.upper()).encode('utf-8')).hexdigest()
res = res.upper()
print(res)





# md5_url = md5(url.encode('utf8')).hexdigest()
# print(md5_url)  # 2f7108ac307fd06f5995948f35a70f2f
#
# response = requests.get(url)
# md5_content = md5(response.content).hexdigest()
# print(md5_content)  # bf93cde0b6edb50b9e95106c11fdd5ad


from random import Random
import hashlib


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    random = Random()
    for i in range(length):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    return salt


# 获取原始密码+salt的md5值
def create_md5(pwd, salt):
    md5_obj = hashlib.md5()
    md5_obj.update((pwd + salt).encode("utf-8"))
    return md5_obj.hexdigest()


# 原始密码
pwd = '123456'
# 随机生成4位salt
salt = create_salt()
# 加密后的密码
md5 = create_md5(pwd, salt)

print('[pwd]\n', pwd)
print('[salt]\n', salt)
print('[md5]\n', md5)



# e10adc3949ba59abbe56e057f20f883e
