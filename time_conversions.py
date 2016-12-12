#!/usr/bin/python
import datetime
import time

def datetime2epoch(timestamp, pattern="%Y-%m-%d %H:%M:%S"):
    """
    Convert a datetime string to the epoch timestamp. Default pattern is formatted:
    year-month-day hour:minute:second, e.g. '2016-08-10 19:37:51' resulting in 1470850671000
    """
    epoch = int(time.mktime(time.strptime(timestamp, pattern)))*1000
    return epoch

def epoch2localtime(epoch):
    """   
    Convert a epoch timestamp into human readable timestring in the local time of the machine
    """
    timestamp = datetime.datetime.fromtimestamp(float(epoch)/1000.)
    fmt = "%Y-%m-%d %H:%M:%S"
    converted_time =  timestamp.strftime(fmt)
    return converted_time

def epoch2utctime(epoch):
    """   
    Convert a epoch timestamp into human readable timestring in the UTC time
    """
    timestamp = datetime.datetime.utcfromtimestamp(float(epoch)/1000.)
    fmt = "%Y-%m-%d %H:%M:%S"
    converted_time =  timestamp.strftime(fmt)
    return converted_time

# examples of the same timestring
local = epoch2localtime(1470850671000)
utc = epoch2utctime(1470850671000)
epoch = datetime2epoch("2016-08-10 19:37:51")
print "Local:\t",local
print "UTC:\t",utc
print "Epoch:\t",epoch
