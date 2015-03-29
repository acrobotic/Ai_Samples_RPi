#!/usr/bin/env python
#
# PIR                 RPi
# VCC              to 5 V
# GND              to GND
# OUT (0~3.3V TTL) to GPIO18 (12)
#
# 1. LED anode to GPIO18 (12).
# 2. LED cathode to 300 Ohm resistor.
# 3. 300 Ohm resistor to GND.
#
# Use 2 potentiometer knobs on the sensor for sensitivity and triggering
# adjustments.
#
# Sensitivity (Sx):
# [MAX] Turn all the way CCW for detecting motion from over ~10 steps away
# [MIN] Turn all the way CW for detecting motion from at most ~4 steps away
#
# Triggering (Tx):
# [MAX] Turn all the way CCW and the trigger latches for ~20secs when
# motion is detected.  It then takes ~3secs to arm itself for triggering.
# [MIN] Turn all the way CW and the trigger latches for ~1sec when
# motion is detected.  It then takes ~3secs to arm itself for triggering.
#
# Recommend setting Sx and Tx to [MIN] for testing.
#
import time
import RPi.GPIO as GPIO

input_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(input_pin, GPIO.IN)
# On first power-on, PIR sensor will output 0-3 motion sensing pulses, which
# may take up to 30 seconds.
print("Waiting 30 seconds for sensor to initialize")
time.sleep(30)

pir_state = GPIO.input(input_pin)
pir_state_last = pir_state

print("Motion detector started")
while True:
  pir_state = GPIO.input(input_pin)

  if pir_state == GPIO.HIGH and pir_state_last == GPIO.LOW:
    print("Motion started")
  elif pir_state == GPIO.LOW and pir_state_last == GPIO.HIGH:
    print("Motion ended")

  pir_state_last = pir_state

  time.sleep(0.1)

GPIO.cleanup()

