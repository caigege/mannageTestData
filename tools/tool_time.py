import datetime
def getDBtime(timeStamp):
    dateArray = datetime.datetime.fromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime