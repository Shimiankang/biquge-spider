# -*- coding: utf-8 -*-
import requests
from lxml import etree
from lib import IP
import random
import os

'''

小说网址 https://www.bbtxt8.com/
一个小说的接口 https://www.bbtxt8.com/10/10489/              里面有每一章节的接口
每一章节的接口 https://www.bbtxt8.com/10/10489/4535761.html  里面有要爬取的内容

'''
proxies = {
    "http": random.choice(IP.ip)
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
'''
笔趣阁网站地址
https://www.bbtxt8.com
https://www.bqgbe.com
https://www.bqgbi.com
'''

url_name = input("请输入笔趣阁最新网址：")
novel_url = input("请输入要下载小说的网址：")


def get_data():
    # print(headers)
    response = requests.get(novel_url, headers=headers).content.decode("utf-8")
    # print(response)
    novel_info_html = etree.HTML(response)
    # 获取小说名称
    novel_title = "".join(novel_info_html.xpath("//h1/text()"))
    # 获取每一章节名称
    novel_chapters_title = novel_info_html.xpath("//dd/a/text()")
    # 获取每一章节的地址
    novel_charters_url = novel_info_html.xpath("//dd/a/@href")
    # 如果没有就创建一个存放所有小说的目录
    if not os.path.exists('./Novel'):
        os.mkdir("./Novel")
    # 判断小说目录是否已存在
    if not os.path.exists('./Novel/' + novel_title):
        # 根据小说名称创建目录
        os.mkdir("./Novel/" + novel_title)

    for novel_charter_url, novel_charter_title in zip(novel_charters_url, novel_chapters_title):
        # print(novel_charter_title)
        # 拼接小说地址
        novel_charter_url = url_name + novel_charter_url
        # print('章节名称：',novel_charter_title,'\n地址：',novel_charter_url,)
        try:
            charter_info = requests.get(novel_charter_url, headers=headers, proxies=proxies).content.decode("utf-8")
            charter_info_html = etree.HTML(charter_info)
            charter_content = charter_info_html.xpath("//div[@id='chaptercontent']/text()")
            # print(charter_content)'
            for i in charter_content:
                # print(i)
                with open('./Novel/' + novel_title + "/" + novel_charter_title + ".txt", "a+", encoding="utf-8") as w:
                    w.write(i.replace('\xa0' * 8, '\n\n'))
        except:
            pass
        print(novel_charter_title + "--下载完成")
