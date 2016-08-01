#!/usr/bin/python
import os
import header

header.init()

os.system('echo "%d" |sudo tee /sys/class/gpio/export' %(header.laserPower))
os.system('echo "out" |sudo tee /sys/class/gpio/gpio%d/direction' %(header.laserPower))
os.system('echo "%d" |sudo tee /sys/class/gpio/export' %(header.laserRelay))
os.system('echo "out" |sudo tee /sys/class/gpio/gpio%d/direction' %(header.laserRelay))
os.system('echo "%d" |sudo tee /sys/class/gpio/export' %(header.pumpRelay))
os.system('echo "out" |sudo tee /sys/class/gpio/gpio%d/direction' %(header.pumpRelay))
os.system('echo "%d" |sudo tee /sys/class/gpio/export' %(header.EMsc))
os.system('echo "out" |sudo tee /sys/class/gpio/gpio%d/direction' %(header.EMsc))
