#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='abc123456',
                       charset='utf8', database = 'django_spider')
cursor = conn.cursor()
sql = "select * from spider_tasks"
try:
    cursor.execute('select * from spider_tasks')
    results = cursor.fetchall()
    print("id","create_time","status","git_name")
    for row in results:
        id = row[0]
        print(id)
        create_time = row[1]
        print(create_time)
        status = row[2]
        print(status)
        git_name = row[3]
        print(git_name)
except Exception as e:
    raise e
finally:
    conn.close()