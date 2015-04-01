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

The C example leverages the [WiringPi](http://wiringpi.com/) library which needs to be installed using the following commands. This library is inspired by the [Arduino](http://www.arduino.cc/) [wiring](http://wiring.org.co/) API.

1. `git clone git://git.drogon.net/wiringPi`
1. `cd wiringPi`
1. `./build`

### Run

1. `gcc -o blink blink.c -lwiringPi`
1. `sudo ./blink`

## JavaScript

The JavaScript example uses [Node.JS](https://nodejs.org/) and a Raspberry Pi 2 and Node.JS 0.12.0 compatible fork of the [wiring-pi](https://github.com/nekuz0r/wiring-pi/tree/incoming-node-v0.12.x) wiringPi JavaScript bindings.

### Setup

1. `wget http://node-arm.herokuapp.com/node_latest_armhf.deb`
1. `sudo dpkg -i node_latest_armhf.deb`
1. `npm install git+https://git@github.com/nekuz0r/wiring-pi.git#incoming-node-v0.12.x`

### Run

1. `sudo node blink.js`

# WebIOPi

Web client and API to control the Raspberry Pi's I/O.

## Setup

1. `wget http://downloads.sourceforge.net/project/webiopi/WebIOPi-0.7.1.tar.gz`
1. `tar xvzf WebIOPi-0.7.1.tar.gz`
1. `cd WebIOPi-0.7.1`
1. `patch -p0 -i ../webiopi_raspberry_pi_2_cpu_support.patch`
1. `patch -p0 -i ../webiopi_raspberry_pi_2_gpio_40_pin.patch`
1. `patch -p0 -i ../webiopi_raspberry_pi_2_gpio_mapping.patch`
1. `sudo ./setup.sh`

## Run

1. `sudo /etc/init.d/webiopi start`
1. Open [http://raspberrypi:8000/app/gpio-header](http://raspberrypi:8000/app/gpio-header) from any device on your network. Use the IP address if DNS is not set up.
 * Default user is "webiopi" and password is "raspberry".
1. Change GPIO 18 mode from "IN" to "OUT". 
1. Click "12" to toggle GPIO 18 from HIGH and turn on LED.

1. To auto start WebIOPi `sudo update-rc.d webiopi defaults`

See [INSTALL](https://code.google.com/p/webiopi/wiki/INSTALL#Running_WebIOPi) for other installation options.

