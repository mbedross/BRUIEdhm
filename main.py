"""
Date Created: 2016.04.06
Author: Manu

This function is a wrapper that listens over a UDP port for microscope OPERATION commands. Command list is below.

Manu's MacBook Pro's IP in the wind tunnel is 192.168.1.14 (port is arbitrary)

"""

import socket
import time
import datetime
import re
import subprocess
##import runDHM            # external .py script that runs DHM
import header            # declaration file to initialize super global variables

## Message list
a = 'DHM_on'                                   # Turn on Laser (prepare for DAQ)
b = 'DHM_off'                                  # Turn off laser
c = 'DHM_record'                               # Record holograms
## 'c' should be followed by integer for DAQ time
d = 'DHM_status'                               # Query for DHM status
e = 'DHM_newSample'                            # Turn on pump for new sample
f = 'DHM_auto'                                 # Let DHM run its own cycle
z = 'SYS_off'                                  # Non-emergency shutdown
header.init()                           # Define global variables from header.py

# Status variables
laserStat = 'off'
pumpStat = 'off'

def time_stamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S %Y.%m.%d')
    return (st, ts)

def temp_reading():
    subprocess.call(["sudo","%s/tempReading.py" % (header.GPIOfolder)])
    return
    
(st,ts) = time_stamp()
file = open('%s/EventLog.txt' % (header.filefolder), "a")
print >>file, st, "- DHM powered up"
file.close

## User defined parameters
UDP_IP = "192.168.1.14"
UDP_PORT = 5005
MESSAGE = "Hello, BRUIE! -DHM\n"         ## Sent to server to establish connection

file = open('%s/EventLog.txt' % (header.filefolder), "a")
print >>file, "UDP target IP:", UDP_IP
print >>file, "UDP target port:", UDP_PORT
file.close

## Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

(st,ts) = time_stamp()
file = open('%s/EventLog.txt' % (header.filefolder), "a")
print >>file, st, "- Socket created:", UDP_IP, ":", UDP_PORT
file.close

## Send MESSAGE to verify connection
(st,ts) = time_stamp()
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
file = open('%s/EventLog.txt' % (header.filefolder), "a")
print >>file, st, "- Initialization message sent over UDP"
print >>file, st, "- Waiting for commands..."
file.close
    
def turn_on_laser():
    subprocess.call(["sudo","%s/turnOnLaser.py" % (header.GPIOfolder)])
    (st,ts) = time_stamp()
    file = open('%s/EventLog.txt' % (header.filefolder), "a")
    print >>file, st, "- Laser On"    # Print to log file
    file.close
    laserStat = 'on'
    message = "Laser is " + laserStat + "\n"
    sock.sendto(message, (UDP_IP, UDP_PORT))
    return laserStat

def turn_off_laser():
    subprocess.call(["sudo","%s/turnOffLaser.py" % (header.GPIOfolder)])
    (st,ts) = time_stamp()
    file = open('%s/EventLog.txt' % (header.filefolder), "a")
    print >>file, st, "- Laser Off"
    file.close
    laserStat = 'off'
    message = "Laser is " + laserStat + "\n"
    sock.sendto(message, (UDP_IP, UDP_PORT))
    return laserStat

def record(data):
    camtime = map(int, re.findall(r'\d+', data))  # Extract camtime from command
    camTime = camtime[0]
    ##runDHM.rover(camTime)                   # Call function run from DHM_recordHolo (imported)
    message = "- DHM recorded for" + camtime + "seconds\n"
    (st,ts) = time_stamp()
    file = open('%s/EventLog.txt' % (header.filefolder), "a")
    print >>file, st, message
    file.close
    sock.sendto(message, (UDP_IP, UDP_PORT))
    return

def status():
    ## This subroutine sends a datagram through UDP of the status of the DHM
    
    (st,ts) = time_stamp()
    STATUS = st + '- Laser is ' + laserStat + ', Pump is ', pumpStat, '- camera temperature is ', CAMTEMP, "\n"
    sock.sendto(STATUS, (UDP_IP, UDP_PORT))
    return

def new_sample():
    ## This subroutine runs the pump for a predetermined time in order to cycle
    ## in a new sample to be imaged
    
    ## subprocess.call(["python",newSample])
    subprocess.call(["sudo","%s/newSample.py" % (header.GPIOfolder)])
    (st,ts) = time_stamp()
    file = open('%s/EventLog.txt' % (header.filefolder), "a")
    print >>file, st, "- New sample was pumped into sample chamber"
    MESSAGE = st + "- New sample was pumped into sample chamber\n"
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    file.close
    return

def auto_run():
    ## This subroutine allows the DHM to run a predefined DAQ protocol that is
    ## not dictated by the BRUIE
    
    ##runDHM.auto()
    (st,ts) = time_stamp()
    file = open('%s/EventLog.txt' % (header.filefolder), "a")
    print >>file, st, "- New sample was pumped into sample chamber"
    file.close
    return

def power_off():
    ##subprocess.call(["python",powerOff])
    subprocess.call(["sudo","%s/powerOff.py" % (header.GPIOfolder)])
    return

## Export GPIO pins for hardware operation
##subprocess.call(["python",export])
subprocess.call(["sudo","%s/exportGPIO.py" % (header.GPIOfolder)])

file = open('%s/EventLog.txt' % (header.filefolder), "a")
(st,ts) = time_stamp()
print >>file, st, " - GPIO Pins Exported"
file.close

## Begin waiting for commands from BRUIE
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data:
        file = open('%s/EventLog.txt' % (header.filefolder), "a")
        (st,ts) = time_stamp()
        print >>file, st, " - Datagram Received:", data
        file.close
    if a in data: # turn laser on
        laserStat = turn_on_laser()
        
    if b in data: # turn laser off 
        laserStat = turn_off_laser()
        
    if c in data: # DHM_record 
        record(data)
        
    if d in data: # DHM_status
        status()
        
    if e in data: # pump in new sample
        new_sample()
        
    if f in data: # run microscope on auto
        auto_run()
        
    if z in data: # Non-emergency shutdown
        power_off()
