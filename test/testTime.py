#! /usr/bin/env python

'''
# @Create   :2021/3/15 11:16
# @Author   : Admin
# @Description  :   说明文件功能
@Modify Time        @Version    @Description
------------        --------    ------------
2021/3/15 11:16     1.0          '你好'   
'''
import datetime
# from urllib.request import urlopen
import time

import requests

# requests
from tools import tool_time

month_of_days31 = [1, 3, 5, 7, 8, 10, 12]
month_of_days30 = [4, 6, 9, 11]
feb_month = 2
dic = {"workTime14": {"am": {"starTime": "09:00:00", "endTime": "12:00:00"},
                      "pm": {"starTime": "13:30:00", "endTime": "18:00:00"}},
       "workTime5": {"am": {"starTime": "09:00:00", "endTime": "12:00:00"},
                     "pm": {"starTime": "13:30:00", "endTime": "17:30:00"}},
       "workTime67": {"am": {"starTime": "10:00:00", "endTime": "12:00:00"},
                      "pm": {"starTime": "13:30:00", "endTime": "18:00:00"}}}

# 开始时间判断
# 1.判断周几
dtime = datetime.datetime(2001, 3, 13, 13, 23, 37)
print(dtime.hour)


# print(dtime.weekday())
def addWorkTime():
    '''
    加班时间安排 todo
    :return:
    '''


def planTime(planStarTime, planEndTime, judgeStata, judgeTimes):
    '''

    :param planStarTime:  工作时间开始时间
    :param planEndTime:   工作时间结束时间 planEndTime 上午 11 下午5
    :param judgeStata: 1:前一个工作有“ 需要判断的日期如 3月20日” 的工作时间 2:否则反之
    :param judgeTime: 需要判断的日期 1.[] 小于工作时间开始最早的开始对象    2.[[],[],[]] 在工作时间节点内开始的对象
    :return: True 有时间可安排， False 没时间可安排
    '''

    if judgeStata == 1:
        judgeStartTime = judgeTimes[0]
        judgeEndTime = judgeTimes[1]
        if judgeEndTime <= planEndTime:
            #             有时间可安排
            return True
        else:
            # 没时间可安排
            return False
    elif judgeStata == 2:
        for jT in judgeTimes:
           res= planTime(planStarTime, planEndTime, 1, jT)
           if not res :
               return res
        return res


def startTimeJudge(dtime):
    '''

    :param dtime: 工作开始时间（模糊的）精确到日，不是当前时间给出提示
    :return: 系统工作开始时间 精确到时
    '''
    week = dtime.weekday()
    hour = dtime.hour
    mius = dtime.minute
    Year = dtime.year
    Mouth = dtime.month
    Day = dtime.day
    workDayData = str(Year) + "-" + str(Mouth) + "-" + str(Day)

    if tool_time.getTimeStamp(datetime.datetime.now()) > tool_time.getTimeStamp(dtime):
        #     用当前时间

        return startTimeJudge(datetime.datetime.now())
    else:
        #      传入时间

        if week <= 4:
            if hour > 17:
                #    下个工作日 时间从9:00开始
                s = dtime + datetime.timedelta(days=workDay(workDayData)).strftime("%Y-%m-%d %H:%M:%S")
                print("s:" + s)
            # elif (hour>13 or (hour==13 and mius>=30)) and hour<=17:
            elif hour > 11 and hour <= 17:
                if hour == 17 and mius > 0:
                    #      下个工作日 时间从9:00开始
                    dtime + datetime.timedelta(days=workDay(workDayData)).strftime("%Y-%m-%d %H:%M:%S")

                    pass
                # 下午安排

                pass
            elif hour <= 11:
                # 上午安排
                pass


        elif week == 5:

            if hour > 17:
                #     加3天 时间从9:00开始
                pass
                # elif (hour>13 or (hour==13 and mius>=30)) and hour<=17:
            elif hour > 11 and hour <= 17:
                if hour == 17 and mius > 0:
                    #      加3天 时间从9:00开始
                    pass
                # 下午安排

                pass
            elif hour <= 11:
                # 上午安排
                pass

        elif week == 6:
            if hour > 17:
                #     加2天 时间从10:00开始
                pass
                # elif (hour>13 or (hour==13 and mius>=30)) and hour<=17:
            elif hour > 11 and hour <= 17:
                if hour == 17 and mius > 0:
                    #      加2天 时间从10:00开始
                    pass
                # 下午安排

                pass
            elif hour <= 11:
                # 上午安排
                pass
        return datetime.datetime(2022, 3, 12, 10, 23, 37)


def workDay(date):
    '''
    获取假日安排
    :param:date “2000-1-2
    :return: 假日天数

    '''
    # todo
    '''
    http://timor.tech/api/holiday/info/2020-10-31
    type 0工作日 1周末 2节假日3调休
    “code”:0,“type”:{“type”:0,“name”:“周五”,“week”:5},“holiday”:null}
    '''
    num = 1  # "计数器"
    while True:
        url = r'http://timor.tech/api/holiday/info/' + date
        # http://timor.tech/api/holiday/info/2021-03-15
        print("url:" + url)
        s = requests.get(url)
        print(type(s.json()), s.json())
        res = s.json()
        time.sleep(2)
        dates = date.split("-")
        Year = dates[0]
        Mouth = dates[1]
        Day = dates[2]

        if res["type"]["type"] != 0:
            # 假日
            num = num + 1
            Day = int(Day) + 1
            error_msg = validate_param(int(Year), int(Mouth), int(Day))
            if error_msg == 3:
                Day = 1;
                Mouth = int(Mouth) + 1
                error_msg2 = validate_param(int(Year), Mouth, Day)
                if error_msg2 == 2:
                    Year = int(Year) + 1

            date = str(Year) + "-" + str(Mouth) + "-" + str(Day)
        else:
            return num


def get_day_of_year(year, month, day):
    """
    获取一个日期在这一年中的第几天
    :param year: 年份
    :param month: 月份
    :param day: 日期
    :return: 在这一年中的第几天
    """
    # 参数校验
    error_msg = validate_param(year, month, day)
    if error_msg:
        return error_msg

    if month == 1:
        return day

    if month == 2:
        return day + 31

    days_of_31_num = 0
    days_of_30_num = 0
    # 31天月份数
    for days_of_31 in month_of_days31:
        if days_of_31 < month:
            days_of_31_num += 1
        else:
            break

    # 30天月份数
    for days_of_30 in month_of_days30:
        if days_of_30 < month:
            days_of_30_num += 1
        else:
            break

    return days_of_31_num * 31 + days_of_30_num * 30 + (29 if is_leap_year(year) else 28) + day


def validate_param(year, month, day):
    """
    参数校验
    :param year: 年份
    :param month: 月份
    :param day: 日期
    :return: error_msg 错误信息，没有为空
    """
    error_msg = u''
    if not isinstance(year, int) or year < 1:
        error_msg = 1
        # u'年份输入不符合要求'
    if not isinstance(month, int) or month < 1 or month > 12:
        error_msg = 2
        # u'月份输入不符合要求'
    if not isinstance(day, int) or day < 1 \
            or (month in month_of_days31 and day > 31) \
            or (month in month_of_days30 and day > 30) \
            or (month == feb_month and (day > 29 if is_leap_year(year) else day > 28)):
        error_msg = 3
        # u'日期输入不符合要求'
    return error_msg


def is_leap_year(year):
    """
    判断当前年份是不是闰年，年份公元后，且不是过大年份
    :param year: 年份
    :return: True 闰年， False 平年
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def getNextDay(date):
    # "".split()
    dates = date.split("-")
    Year = dates[0]
    Mouth = dates[1]
    Day = dates[2]
    if is_leap_year(int(Year)):
        #     润年

        pass
    else:
        #     平年

        pass

    return


print(startTimeJudge(dtime))
print(dtime.month)
print(get_day_of_year(dtime.year, dtime.month, dtime.day))
print(workDay("2020-1-31"))
