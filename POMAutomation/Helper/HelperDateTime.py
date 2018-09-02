import datetime
import time
from dateutil import relativedelta

class HelperDateTime(object):

    @staticmethod
    def GetPresentTime():
        CurrentTime = datetime.datetime.now()
        return CurrentTime

    @staticmethod
    def GetTimeDifferenceInMinute(PastTime):
        CurrentTime = HelperDateTime.GetPresentTime()
        TimeDifference = relativedelta.relativedelta(CurrentTime,PastTime)
        return TimeDifference.minutes

    @staticmethod
    def GetTimeDifferenceInSecond(PastTime):
        CurrentTime = HelperDateTime.GetPresentTime()
        TimeDifference = relativedelta.relativedelta(CurrentTime,PastTime)
        return TimeDifference.seconds

    @staticmethod
    def GetTimeStamp(FormatTimeStamp='%Y_%m_%d_%H_%M_%S'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTimeStamp)

    @staticmethod
    def GetCurrentTime(FormatTime='%H:%M:%S'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTime)

    @staticmethod
    def GetCurrentDate(FormatTimeStamp='%Y-%m-%d'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTimeStamp)

    @staticmethod
    def GetCurrentDateTime(FormatTimeStamp='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTimeStamp)