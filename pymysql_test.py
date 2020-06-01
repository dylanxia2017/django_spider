#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='abc123456',
                       charset='utf8', database = 'django_spider')
cursor = conn.cursor()

# 建库建表
sql = "select * from spider_tasks where status = 0"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(len(results))
except Exception as e:
    raise e
finally:
    conn.close()

# sql = "select * from spider_tasks"
# try:
#     cursor.execute('select * from spider_tasks')
#     results = cursor.fetchall()
#     print("id","create_time","status","git_name")
#     for row in results:
#         id = row[0]
#         print(id)
#         create_time = row[1]
#         print(create_time)
#         status = row[2]
#         print(status)
#         git_name = row[3]
#         print(git_name)
# except Exception as e:
#     raise e
# finally:
#     conn.close()


# 插入操作
# time_local = time.localtime()
# ow_times = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
# create_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
# # print(time.strftime("%Y-%m-%d %H:%M:%S", time_local))
# git_name = "dylanxia2017" + ow_times
#
# sql_insert = "insert into spider_tasks(create_time,status, git_name) values ('%s','0','%s')" % (create_time, git_name)
# try:
#     cursor.execute(sql_insert)
#     conn.commit()
#     print("开始数据库插入操作")
# except Exception as e:
#     conn.rollback()
#     print("数据库回滚")
# finally:
#     conn.close()

# 更新操作
# sql_update = "update django_spider.spider_tasks set status = '1' where git_name = 'dylanxia20172020-06-01-20-50-50'"
# try:
#     cursor.execute(sql_update)
#     conn.commit()
#     print("开始数据库更新操作")
# except Exception as e:
#     conn.rollback()
#     print("数据库更新操作错误回滚")
# finally:
#     conn.close()