Raspberry Pi 2 DS18B20 1-Wire Digital Thermometer
=================================================

# Setup

## Hardware

RPI        to DS18B20
Ground (5)    GND (1/Black)
3.3V   (1)    VDD (3/Red)
GPIO04 (7)    DQ  (2/White)

Connect a 4.7k Ohm resister between VDD and DQ to act as a pull-up.

## Software

1. `sudo sh -c 'echo "dtoverlay=w1-gpio,gpiopin=4" >> /boot/config.txt`
1. `sudo sh -c 'echo "w1_gpio\nw1_therm" >> /etc/modules` 
1. `sudo reboot`

# Demo

1. `sudo ./ds18B20.py`

