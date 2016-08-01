# BRUIEdhm

This operation software is meant to run the BRUIE DHM device.

File Desicriptions are as follows:

1. main.py
2. header.py
2. exportGPIO.py
3. turnOnLaser.py
4. turnOffLaser.py
5. newSample.py
6. tempReading
7. unexportGPIO.py
8. powerOff.py

--------------------------------------------------------------------------------------------------------------------------------------

1. This is the main wrapper function that calls all other subroutines. It establishes a UDP connection with BRUIE and waits for commands. The command list and actions are as follows:

  a. 'DHM_on' turns the laser on and prepares the system for DAQ
  b. 'DHM_off' turns the laser off
  c. 'DHM_record xx' Acquires data for xx seconds
  d. 'DHM_status' requests diagnostic information from the DHM (laser status, temperature, etc)
  e. 'DHM_newSample' runs the fluidic pump to cycle in a new sample into the DHM
  f. 'DHM_auto' Runs the DHM on a preprogramed cycle (fixed framrate and camera time)
  g. 'SYS_off' turns the system off
  
2. This script establishes consistant naming between scripts. Declares global variables that are used throughout the OS

3. 
