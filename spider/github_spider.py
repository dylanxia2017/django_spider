#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from time import sleep

def git_spider(url):
    req = requests.get(url)
    sleep(10)
    parsedData = []
    jsonList = []
    jsonList.append(req.json())
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)
    message = "爬虫成功!!"
    return parsedData, message