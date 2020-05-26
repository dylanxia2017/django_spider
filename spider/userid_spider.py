#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import json



def get_userinfo(idcard):
    user_info = {}
    user_data = []
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
        }
    url = 'http://qq.ip138.com/idsearch/index.asp?action=idcard&userid={}'.format(idcard)

    r = requests.get(url,headers=headers)
    # print(r.content.decode("utf-8"))
    a = re.findall('<p>发证地</p></td><td><p>(.*?)<br/></p></td></tr>',r.content.decode('utf-8'))
    message = "提取用户的信息完成"
    if a == []:
        user_info['idcard'] = idcard
        user_info['area'] = ''
        user_data.append(user_info)
        return user_data, message
    else:
        user_info['idcard'] = idcard
        user_info['area'] = a[0]
        user_data.append(user_info)
        return user_data, message

