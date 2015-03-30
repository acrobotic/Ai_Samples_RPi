Raspberry Pi 2 Super LEDs (APA-102) Demo
========================================

# Wiring

Requires a separate 5 V / 2+ A power supply and a level shifter for the SPI signals.

# Setup

1. `git clone https://github.com/adafruit/Adafruit_DotStar_Pi`
1. `cd Adafruit_DotStar_Pi`
1. `make`
1. `sudo raspi-config`
1. Select "Advanced Options" > SPI
1. Select Yes to enable and Yes to load driver module automatically on boot.
1. Select Finish

# Run

1. `sudo python strandtest.py`

