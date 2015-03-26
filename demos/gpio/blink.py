#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

led_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

for i in range(0,30):
  GPIO.output(led_pin, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(led_pin, GPIO.LOW)
  time.sleep(1)

GPIO.cleanup()

