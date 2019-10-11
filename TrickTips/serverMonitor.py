"""
Script will check the server status and notify any critical
issue directly on your browser or phone
"""
from notify_run import Notify
from datetime import datetime
import os
import time

# Return CPU temperature as a character string


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "").replace("'C\n", ""))

# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM


def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])

# Return % of CPU used by user as a character string


def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(
)))

# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used


def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:5])


if __name__ == "__main__":
    RAM_stas = getRAMinfo()
    RAM_free = round(int(RAM_stas[1]) / 1000,1)
    # RAM_free = 900
    DISK_stats = getDiskSpace()
    DISK_free = DISK_stats[2]
    notify = Notify()
    count = 0
    
    while True:
        count += 1
        print("CONTINOUSLY RUNNING {}".format(count))
        print("FREE DISK SPACE: {} and FREE RAM SIZE: {}".format(DISK_free, RAM_free))
        if int(DISK_free.split('G')[0]) < 5 :
            notify.send("!!! CRITICAL CRITICAL !!!! Please check the server right now. The Disk size is lower than {}".format(DISK_free))        
        
        if RAM_free < 1000:
            notify.send("Whooops ! The Free ram size is available around {}MB".format(RAM_free))            
        time.sleep(5)