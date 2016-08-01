#!/usr/bin/python
import os
import header
import time

header.init()

count = 1
while (count < 50):
    os.system('echo "1" |sudo tee /sys/class/gpio/gpio%s/value' %(header.pumpRelay))
    time.sleep(0.03)
    os.system('echo "0" |sudo tee /sys/class/gpio/gpio%s/value' %(header.pumpRelay))
    time.sleep(0.03)
    count = count + 1
