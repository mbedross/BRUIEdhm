#!/usr/bin/python
import os
## REMEMBER TO ADD LINE TO ADD HEADER FILEPATH TO SYSTEM PATH BEFORE IMPORTING HEADER FILE!!!
import header
import time

header.init()

## Turn laser Relay off, and set power off (1.8V)

os.system('echo "0" |sudo tee /sys/class/gpio/gpio%s/value' %(header.laserPower))
time.sleep(1)
os.system('echo "0" |sudo tee /sys/class/gpio/gpio%s/value' %(header.laserRelay))
