# -*- coding: utf-8 -*-
"""
@Time ： 2023/10/13 0013 10:06
@Auth ： imdatouk
@File ：main.py
@IDE ：PyCharm
@Email: imdatouk@outlook.com
"""
import threading
import src.Spider as Spider

if __name__ == "__main__":
    main = threading.Thread(target=Spider.get_data)
    main.start()