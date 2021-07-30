# -*- coding: utf-8 -*-
"""
作者: holmes
日期: 2021年 07月 2021/7/28日 14:03
"""
'''
--------------------------------- 数据驱动 测试案例
测试xxx项目接口的异常场景
pytest abtest\testcases\test_unnormal.py -s
为啥加s 可以看结果:  
pytest -v abtest\testcases\test_unnormal.py
查看日志: 
'''
import requests
import pytest
import abtest.business.common as common
import json
from abtest.business.file_utils import parse_json_file

###  {传的参数}, 预期响应码，预期响应msg
# test_data = [
#     ({"accesstoken": "","title": "(数据驱动01)tes主题727_001","tab": "ask","content": "12345678-727ce"},401,"错误的accessToken"),
#     ({"accesstoken": "","title": "","tab": "ask","content": "12345678-727"},401,"错误的accessToken"),
#     ({"accesstoken": "","title": "tes主题727_001","tab": "ask","content": "12345678-727ce1"},401,"错误的accessToken"),
#     ({"accesstoken": common.get_token(),"title": "tes主题727_001","tab": "","content": "8-727"},400,"必须选择一个版块")
# ]

### 数据驱动, 读取  数据文件json
# data = json.load(open("D:/AutoApi/autotest_xudada_07/abtest/data/topics.json", mode="r", encoding="utf8"))  # 加载权限
# test_data = data['test_data']


test_data =parse_json_file("D:/AutoApi/autotest_xudada_07/abtest/data/topics.json")

@pytest.mark.parametrize("topic_data,R_status_code,R_msg",test_data)
def test_creat_topic(topic_data,R_status_code,R_msg):
    print(topic_data,R_status_code,R_msg)
    res = requests.post("http://47.100.175.62:3000/api/v1/topics",topic_data)

    print(res.json())

    assert res.status_code ==R_status_code
    assert res.json()["error_msg"] == R_msg
