# BRUIEdhm

This operation software is meant to run the BRUIE DHM device.

File Desicriptions are as follows:

1. main.py
2. header.py
3. exportGPIO.py
4. turnOnLaser.py
5. turnOffLaser.py
6. newSample.py
7. tempReading
8. unexportGPIO.py
9. powerOff.py

--------------------------------------------------------------------------------------------------------------------------------------

1. This is the main wrapper function that calls all other subroutines. It establishes a UDP connection with BRUIE and waits for commands. The command list and actions are as follows:

a. 'DHM_on' turns the laser on and prepares the system for DAQ
b. 'DHM_off' turns the laser off
c. 'DHM_record xx' Acquires data for xx seconds
d. 'DHM_status' requests diagnostic information from the DHM (laser status, temperature, etc)
e. 'DHM_newSample' runs the fluidic pump to cycle in a new sample into the DHM
f. 'DHM_auto' Runs the DHM on a preprogramed cycle (fixed framrate and camera time)
g. 'SYS_off' turns the system off

After establishing a UDP connection with BRUIE, it will 'export' all necessary GPIO pins then wait for any of the above commands and execute them as necessary.

-
  
2. This script establishes consistant naming between scripts. Declares global variables that are used throughout the OS

-

3. This script 'exports' the GPIO pins on the Odroid. This means that it declare which pins are going to be used, assigns names and declares them as outputs. It also initializes the ADC pin in order to take temperature measurements.

-

4. Turns on the laser by using the GPIO pin on the Odroid to switch a relay, giving the laser power via 12Vdc power supply. This script is called when the 'DHM_on' command is received.

-

5. Deenergizes the relay that powers the laser thus turning it off. This script os called when the 'DHM_off' command is received.

-

6. This script runs the fluidic pump for 15 seconds in order to cycle in new sample into the sample chamber. This script is called when the 'DHM_newSample' command is received, and when the 'DHM_on' command is received in order to prime the sample chamber and prepare it for DAQ.

-

7. This scripts reads the voltage across the termistor and calculates the temperature of the sample by using the Steinhart-Hart Equation. More information on the wiring schematic of the termistor setup can be found in the 'supp.materials' branch. This script is called when the 'DHM_status', 'DHM_record', 'DHM_auto', or 'DHM_newSample' commands are received.

-

8. This script 'unexports' the GPIO pins. It declares the puins no longer in use and so the Odroid no longer devote power or memory towrds them. This is called when the 'SYS_off' command is recieved.

-

9. This script powers off the DHM system. It turns off all GPIO ports and shuts down the Odroid.
