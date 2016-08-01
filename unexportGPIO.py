#!/usr/bin/python
import os
import header

header.init()

os.system('echo "%d" |sudo tee /sys/class/gpio/unexport' %(header.laserPower))
os.system('echo "%d" |sudo tee /sys/class/gpio/unexport' %(header.laserRelay))
os.system('echo "%d" |sudo tee /sys/class/gpio/unexport' %(header.pumpRelay))
os.system('echo "%d" |sudo tee /sys/class/gpio/unexport' %(header.EMsc))
