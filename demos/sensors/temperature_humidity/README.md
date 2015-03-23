Raspberry Pi 2 RHT-03 (aka DHT-22) Digital Temperature and Humidity Sensor
==========================================================================

Setup
=====

1. `sudo apt-get update`
1. `sudo apt-get install build-essential python-dev`
1. `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
1. `cd Adafruit_Python_DHT`
1. `sudo python setup.py install`

Example
=======

1. Connect from left to right:
 1. Pin 1 to 3.3 V
 2. Pin 2 to GPIO22 (15)
 3. Pin 3 Not Connected
 4. Pin 4 to GND
2. Connect a pull-up 10k Ohm resistor from signal pin 2 to Vdd pin 1.

1. `cd examples`
1. `sudo ./AdafruitDHT.py 22 22`

    ````
    Temp=23.4*C  Humidity=46.8%
    ````

