#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1.打开url
_url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/"
html = urlopen(_url + "index.html")

# 2.解析URL下的页面内容
bsObj = BeautifulSoup(html, features="lxml")
# 3.查找目标数据
provincetr_list = bsObj.findAll(class_="provincetr")
for provincetr in provincetr_list:
    for provincetd in provincetr.findAll("td"):
        a = provincetd.find("a")
        if a is None:
            continue
        print(a.get_text())
        html = urlopen(_url + a["href"])
        bsObj = BeautifulSoup(html, features="lxml")
        citytr_list = bsObj.findAll(class_="citytr")
        for citytr in citytr_list:
            a = citytr.findAll("td")[1].find("a")
            if a is "市辖区":
                continue
            print("\t" + a.get_text())
# 4.存储目标数据
