# -*- encoding: utf-8 -*-

"""
@File    :   demo3.py    
2021/10/18 18:15     Xchen~      
"""

# &#xf6e2;
from fontTools.ttLib import TTFont

font = TTFont('8160b98d.woff')
font.saveXML('8160b98d.xml')
camp = font['cmap'].getBestCmap()
ids = font.glyphOrder[1:]
print(ids)
new_camp = {}
map_ = {}
for code, name in camp.items():
    code = str(hex(code)).replace('0', '&#', 1) + ';'
    map_[name] = code

nums = ['.', 3, 1, 2, 9, 7, 5, 8, 0, 6, 4]
nums1 = ['.',2,1,7,6,5,0,8,4,3,9]
nums2 = ['.',5,6,0,3,1,2,8,4,9,7]
nums3 = ['.',0,7,2,4,8,6,1,3,5,9]
nums4 = ['.',0,4,2,1,9,7,6,8,3,5]
nums5 = ['.',6,2,8,4,5,9,0,7,1,3]
for id, num in zip(ids, nums5):
    new_camp[num] = map_[id]
print(new_camp)


"""
第一套
&#xe582      1 
{'.': '&#x78;', 2: '&#xee24;', 1: '&#xe582;', 7: '&#xec83;', 6: '&#xecea;', 5: '&#xf81e;', 0: '&#xe33b;', 8: '&#xf2d2;', 4: '&#xf8a6;', 3: '&#xe93b;', 9: '&#xeb12;'}
['x', 'uniEE24', 'uniE582', 'uniEC83', 'uniECEA', 'uniF81E', 'uniE33B', 'uniF2D2', 'uniF8A6', 'uniE93B', 'uniEB12']

第二套
&#xed83      1
{'.': '&#x78;', 3: '&#xe324;', 1: '&#xed83;', 2: '&#xf4cd;', 9: '&#xefdc;', 7: '&#xf0d7;', 5: '&#xe9ac;', 8: '&#xf4a6;', 0: '&#xf076;', 6: '&#xe6cd;', 4: '&#xf2da;'}
['x', 'uniE324', 'uniED83', 'uniF4CD', 'uniEFDC', 'uniF0D7', 'uniE9AC', 'uniF4A6', 'uniF076', 'uniE6CD', 'uniF2DA']

第三套
&#xf6e2      1 
{'.': '&#x78;', 5: '&#xf43c;', 6: '&#xe68f;', 0: '&#xf483;', 3: '&#xe3ad;', 1: '&#xf6e2;', 2: '&#xf40a;', 8: '&#xeb35;', 4: '&#xea6f;', 9: '&#xe80a;', 7: '&#xec34;'}
['x', 'uniF43C', 'uniE68F', 'uniF483', 'uniE3AD', 'uniF6E2', 'uniF40A', 'uniEB35', 'uniEA6F', 'uniE80A', 'uniEC34']

第四套
&#xe7c3     1
{'.': '&#x78;', 0: '&#xe341;', 7: '&#xe9a8;', 2: '&#xf4ff;', 4: '&#xe0c5;', 8: '&#xeb75;', 6: '&#xedca;', 1: '&#xe7c3;', 3: '&#xec3d;', 5: '&#xf58b;', 9: '&#xf2de;'}
['x', 'uniE341', 'uniE9A8', 'uniF4FF', 'uniE0C5', 'uniEB75', 'uniEDCA', 'uniE7C3', 'uniEC3D', 'uniF58B', 'uniF2DE']

第五套
xeb93 1
{'.': '&#x78;', 6: '&#xf87e;', 2: '&#xf832;', 8: '&#xf131;', 4: '&#xe7a5;', 5: '&#xf53d;', 9: '&#xf8bf;', 0: '&#xf173;', 7: '&#xeff2;', 1: '&#xeb93;', 3: '&#xe532;'}
['x', 'uniF87E', 'uniF832', 'uniF131', 'uniE7A5', 'uniF53D', 'uniF8BF', 'uniF173', 'uniEFF2', 'uniEB93', 'uniE532']
第六套 
&#xf0b9 1
{'.': '&#x78;', 0: '&#xe5e4;', 4: '&#xed98;', 2: '&#xe0fd;', 1: '&#xf0b9;', 9: '&#xec34;', 7: '&#xee3d;', 6: '&#xea43;', 8: '&#xf10a;', 3: '&#xece7;', 5: '&#xf460;'}
['x', 'uniE5E4', 'uniED98', 'uniE0FD', 'uniF0B9', 'uniEC34', 'uniEE3D', 'uniEA43', 'uniF10A', 'uniECE7', 'uniF460']
"""

# https://i.waimai.meituan.com/external/ajax/getsecretcssresource