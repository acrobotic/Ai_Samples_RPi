#!/usr/bin/env python
#
import time
import RPi.GPIO as GPIO

input_pin = 12
pir_state = GPIO.LOW
pir_state_last = pir_state

GPIO.setmode(GPIO.BOARD)
GPIO.setup(input_pin, GPIO.IN)
# PIR sensor will output 0-3 motion sensing pulses during initialization. 
# This may take up to 30 seconds and is applicable only on first power-on.
#print("Waiting 30 seconds to initialize sensor")
#time.sleep(30)

print("Motion detector started")
while True:
  pir_state = GPIO.input(input_pin)

  if pir_state == GPIO.HIGH:
    if pir_state_last == GPIO.LOW:
      print("Motion started")
  else:
    if pir_state_last == GPIO.HIGH:
      print("Motion ended")

  pir_state_last = pir_state

  time.sleep(1)

GPIO.cleanup()

