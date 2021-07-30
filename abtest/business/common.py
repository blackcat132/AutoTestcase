# -*- coding: utf-8 -*-
"""
作者: holmes
日期: 2021年 07月 2021/7/27日 17:21
"""
import requests


def creat_topic(topic_params):
    url = "http://47.100.175.62:3000/api/v1/topics"
    #headers = {}
    r = requests.post(url=url, json=topic_params, verify=False)   #注意这是json 是放在body里的

    return r


def topic_detail(id):
    url = "http://47.100.175.62:3000/api/v1/topic/" + id
    return requests.get(url)


def get_token():
    return  '1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694'


    # response = requests.request("GET", url=url_01, headers=headers, data=payload, verify=False)
    #
    # url_01 = "http://47.100.175.62:3000/api/v1/topics"
    #
    # payload = {'accesstoken': '1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694',
    #            'title': 'test主题727',
    #            'tab': 'ask',
    #            'content': '12345678-727'}
    # headers = {}
    #
    # r = r.request("GET", url=url_01, headers=headers, data=payload, verify=False)
    #
    # print(r.json())
    #
