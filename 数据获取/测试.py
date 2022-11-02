# _*_ coding :utf-8 _*_
# @Time :2022/3/31 15:54
# @Author :河北地质大学 李林逸
# @File : 测试
# @Project :爬虫
import re
import json
import requests
import pprint
import csv


url='https://www.shanghairanking.cn/rankings/bcur/2022'

headers = {
    'cookie':'Hm_lvt_af1fda4748dacbd3ee2e3a69c3496570=1666615832; Hm_lpvt_af1fda4748dacbd3ee2e3a69c3496570=1666615883',
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

html_data = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text)[0]
json_data = json.loads(html_data)

print(json_data)
