# -*- coding: utf-8 -*-
"""
作者: holmes
日期: 2021年 07月 2021/7/29日 17:23
"""
import logging

logger =logging.getLogger('PahxApp')
logger.setLevel(logging.DEBUG)

format = logging.Formatter('[%(asctime)s][%(levelname)s[%(funcName)s]%(message)s')

fl = logging.FileHandler(filename='D:/AutoApi/autotest_xudada_07/abtest/logs/PahxApp.log', mode='a', encoding='utf8')
fl.setFormatter(format)
sl=logging.StreamHandler()
sl.setFormatter(format)


logger.addHandler(fl)
logger.addHandler(sl)



