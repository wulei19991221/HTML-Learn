# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年06月24日11时
# @File: bilbili_gif.py
import requests
import json
import re
import os

base_path = '../练习/bilibili/'
# 1.下载json文件
# url = 'https://api.live.bilibili.com/gift/v4/Live/giftConfig?platform=pc&roomid=21424354'
# with open('../练习/bilibili/images/gif.json', 'a', encoding='utf-8')as f:
# 	result = json.dumps(requests.get(url).json(), indent=4, ensure_ascii=False)
# 	f.write(result)
# 2.下载gif
# data = json.load(open(base_path + 'images/gif.json', 'r', encoding='utf-8'))
# for i in data['data']['list']:
# 	name = i['name']
# 	gif = i['gif']
# 	with open(f'{base_path}images/{name}.gif', 'wb')as f:
# 		f.write(requests.get(gif).content)
# 	print(name + '\t 下载完成')
# 3.写入html
imgs = '{auto-img}'
with open(f'{base_path}哔哩哔哩动画.html', 'r', encoding='utf-8')as f:
	html = f.read()
content = ''
for i in os.listdir(base_path + 'images/'):
	src = './images/' + i
	content += f'<div class="item">\n\t\t<img src="{src}" alt="{i}">\n\t\t<span>{i.split(".")[0]}</span>\n\t</div>'
with open(f'{base_path}哔哩哔哩动画3.0.html', 'w', encoding='utf-8')as f:
	html = html.replace(imgs, content)
	f.write(html)
