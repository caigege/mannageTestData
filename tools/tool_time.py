import datetime
import time

dtimeTest = datetime.datetime(2021, 3, 12, 10, 23, 37)
def getDBtime(timeStamp):
    '''
    时间戳转 dateTime
    :param timeStamp:
    :return:
    '''
    dateArray = datetime.datetime.fromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime
def getTimeStamp(dtime):
    '''
    dateTime 转时间戳
    :param dtime:
    :return:
    '''
    # dtime = datetime.datetime(2021, 3, 12, 10, 23, 37)
    un_time = time.mktime(dtime.timetuple())
    # print( int(un_time))
    return int(un_time)

# todo 字符串转互相dateTime
def strToDateTime(datestr):
    '''
    字符串转互相dateTime
    :param datestr: %Y-%m-%d %H:%M:%S
    :return:
    '''
    return datetime.datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")

def getDayStr(datetime):
    '''
     获取日期
    :param datetime:
    :return: 日期 2000-01-02
    '''
    return dateTimeToStr(datetime).split(" ")[0]
def  dateTimeToStr(datetime):

    '''
    datetime时间格式转str:
    :param 时间
    :return
    '''

    #
    return datetime.strftime("%Y-%m-%d %H:%M:%S")
print(getDayStr(dtimeTest))