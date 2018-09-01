import datetime
class HelperDateTime():
    def GetCurrentTime():
        CurrentTime = datetime.datetime.time(datetime.datetime.now());
        return CurrentTime;

    def GetTimeDifferenceInMin(PastTime):
        CurrentTime = datetime.datetime.time(datetime.datetime.now());
        Min = CurrentTime-PastTime
        return int((Min.seconds // 60) % 60)

    def GetTimeDifferenceInSec():
        pass;