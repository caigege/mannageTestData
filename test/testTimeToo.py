#! /usr/bin/env python

'''
# @Create   :2021/3/15 17:43
# @Author   : Admin
# @Description  :   说明文件功能
@Modify Time        @Version    @Description
------------        --------    ------------
2021/3/15 17:43     1.0          '你好'   
'''
import datetime
# str转时间格式：
dd = '2019-03-17 11:00:00'
dd = datetime.datetime.strptime(dd, "%Y-%m-%d %H:%M:%S")
print(dd,type(dd))

# 时间格式转str:
dc = dd.strftime("%Y-%m-%d %H:%M:%S")
print(dc,type(dc))