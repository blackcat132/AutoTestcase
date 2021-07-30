# -*- coding: utf-8 -*-
"""
作者: holmes
日期: 2021年 07月 2021/7/13日 10:54
"""
## pytest abtest\testcases\top.py
#  执行: 终端:terminal   执行这个命令(路径+文件):
''''
调试整体(pytest +文件路径)：pytest abtest\testcases\top.py     
调试局部(pytest +文件路径+ :: + 函数名):
pytest abtest\testcases\top.py::test_creat_topic  
快速调试: pytest abtest\testcases -s
测试报告： pytest abtest\testcases --html=report.html
'''

# token : 1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694

# /api/v1/topics

import requests
import abtest.business.common as common
from abtest.business.logger import logger

base_url = 'http://47.100.175.62:3000/api/v1'


def test_topic_page():
    query_params = {'page': '1',
                    'tab': 'share',
                    'limit': '1',
                    'mdrender': 'false'}
    # headers = {}

    r = requests.get(base_url + '/topics', params=query_params, verify=False)
    logger.debug(f'发送这条请求:{r}')

    print(r.json())
    assert r.status_code == 200
    assert r.json()['success'] == True

    data = r.json()['data']
    assert len(data) == query_params['limit']
    for topic in data:
        assert topic == query_params['tab']


def test_creat_topic():  # 创建话题

    topic_params = {
        'accesstoken': common.get_token(),
        'title': 'tes主题727_001',
        'tab': 'ask',
        'content': '12345678-727'
    }
    # headers = {}

    r = common.creat_topic(topic_params)
    print(r.json())
    logger.debug(f'发送这条请求:{r}')

    assert r.status_code == 200
    assert r.json()['success'] == True

    r2 = common.creat_topic(topic_params)
    logger.debug(f'发送这条请求:{r}')

    print('这是r2：', r2)
    assert not r.json()['topic_id'] == r2.json()['topic_id']


# "topic_id": "6100c4d37dce1aeb8287d728"

 # 修改话题
def test_topic_update():
    topic_params = {'accesstoken': common.get_token(),
                    'title': 'tes主题727_002',
                    'tab': 'ask',
                    'content': '12345678-727'}
    # headers = {}
    r = common.creat_topic(topic_params)
    id = r.json()['topic_id']  # 响应 topic_id的 值

    update_topic_params = {
        'accesstoken': common.get_token(),
        'title': 'tes主题727_002(更新2)',
        'topic_id': id,
        'tab': 'ask',
        'content': '12345678-727'
    }
    # headers = {}
    r = requests.post(base_url + '/topics/update', update_topic_params)
    print(r.json())
    logger.debug(f'发送这条请求:{r}')

    assert r.json()['topic_id'] == id

    # "topic_id": "6100c4d37dce1aeb8287d728"

### 查看详情
    r_detail = common.topic_detail(id)
    print(r_detail.json())

    detail_json_data =r_detail.json()   # 把响应的json数据， 赋值给detail_json_data 变量
    assert detail_json_data['data']['id']  == id
    assert detail_json_data['data']['tab']  == update_topic_params['tab']
    assert detail_json_data['data']['title'] == update_topic_params['title']
    assert update_topic_params['content'] in detail_json_data['data']['content']