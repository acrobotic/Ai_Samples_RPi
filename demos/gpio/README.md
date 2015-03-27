Raspberry Pi 2 GPIO Demo
========================

# Blink

Blink is the "Hello World" equivalent for hardware developers.

## Wiring

![Fritzing LED Wiring](http://learn.acrobotic.com/uploads/Turning_LED_On.png)

## Python


### Setup

The Python example leverages the [RPi.GPIO](http://sourceforge.net/projects/raspberry-gpio-python/) module which needs to be installed/updated using the following commands.

1. `sudo apt-get update`
1. `sudo apt-get --yes install python-rpi.gpio python3-rpi.gpio`

### Run

1. `sudo python blink.py`

## C

### Setup

The C example leverages the [WiringPi]() library which needs to be installed using the following commands. This library is inspired by the [Arduino](http://www.arduino.cc/) [wiring](http://wiring.org.co/) API.

1. `git clone git://git.drogon.net/wiringPi`
1. `cd wiringPi`
1. `./build`

### Run

1. `gcc -o blink blink.c -lwiringPi`
1. `sudo ./blink`

## JavaScript


