#!/usr/bin/python
import os
import header
import time

header.init()

## Turn laser Relay on, and set power on (1.8V)

os.system('echo "1" |sudo tee /sys/class/gpio/gpio%s/value' %(header.laserRelay))
time.sleep(1)
os.system('echo "1" |sudo tee /sys/class/gpio/gpio%s/value' %(header.laserPower))
