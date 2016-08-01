"""
Date Created: 2016.04.06
Author: Manu

This is a header file for 'UDP_operation_wrapper.py and 'UDP_emergency_wrapper.py'
that defines global variables to be passed along to other external python scripts

Manu's MacBook Pro's IP in the wind tunnel is 192.168.1.14 (port is arbitrary)

"""

def init():
    global filefolder, codefolder, GPIOfolder
    ## Identify eventlog directory
    filefolder = '/home/odroid/Desktop/BRUIEdhm_os/EventLog'
    ## Identify subroutine direcotry
    codefolder = '/home/odroid/Desktop/BRUIEdhm_os/FINAL'
    ## Identify folder for GPIO files
    GPIOfolder = '/usr/bin'
    
    ## GPIO Pin export numbers
    global laserPower, pumpRelay, EMsc, laserRelay, ADC
    laserPower = 33                       ## GPIO pin number
    pumpRelay = 24                        ## GPIO pin number
    EMsc = 25                             ## GPIO pin number
    laserRelay = 23                       ## GPIO pin number
    pumpTime = 10                          ## Pump time to cycle in new sample
    ADC = 24
