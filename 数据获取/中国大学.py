# _*_ coding :utf-8 _*_
# @Time :2022-02-16 16:18
# @Author :河北地质大学 李林逸
# @File : 一次性爬取99页数据
# @Project :爬虫

import re
import requests
import csv


# 从热销网页找出需要的url

f = open('中国大学.csv','a',encoding='utf-8')

csvwriter = csv.writer(f)


url= 'https://www.shanghairanking.cn/rankings/bcur/2022'

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

response = requests.get(url=url_search, headers=headers)
content = response.text
obj = re.compile(r'data-v-3fe7d390>(?P<ranking>.*?).*?<img alt="(?P<university>.*?)" onerror=.*?',re.S)
result = obj.finditer(content)

for it in result:
    dic = it.group('')
    csvwriter.writerow(dic)


f.close()
print('over!')

