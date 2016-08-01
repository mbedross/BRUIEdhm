#!/usr/bin/python
import time
import datetime
import os
import subprocess
import header                                # global variable declarations

header.init()

def time_stamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S %Y.%m.%d')
    return (st, ts)

os.system('echo "0" |sudo tee /sys/class/gpio/gpio%d/value' %(header.laserRelay))
os.system('echo "0" |sudo tee /sys/class/gpio/gpio%d/value' %(header.pumpRelay))
os.system('echo "0" |sudo tee /sys/class/gpio/gpio%d/value' %(header.EMsc))
os.system('echo "0" |sudo tee /sys/class/gpio/gpio%d/value' %(laserPower))
subprocess.call(["sudo","%s/unexportGPIO.py" % (header.GPIOfolder)])
(st,ts) = time_stamp()
file = open('%s/EventLog.txt' % (header.filefolder), "a")
print >>file, st, " - Non-emergency shut down"
file.close
os.system('shutdown -P now')
