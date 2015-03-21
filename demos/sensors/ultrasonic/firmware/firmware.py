#!/usr/bin/env python
# Raspberry Pi 2 HC-SR04 ultrasonic distance sensor demo
#
#
# HC-SR04 to RPi
# GND        GND (J9.7)
# ECHO       GPIO2 (J11.3) through voltage divider (1).
# TRIG       GPIO3 (J11.4) through inverter below (2).
# VCC        5 V (J9.4)
#
# Note: datasheets recommend connecting GND before VCC.
#
#
import signal
import sys
import time
import RPi.GPIO as GPIO

def signal_handler(signal, frame):
  GPIO.cleanup()
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BOARD)
trig_pin = 11
echo_pin = 12
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
time.sleep(1)

GPIO.output(trig_pin, GPIO.LOW)
time.sleep(3)

while True:
  print("Send Trigger")
  GPIO.output(trig_pin, GPIO.HIGH)
  time.sleep(10/1000/1000)
  GPIO.output(trig_pin, GPIO.LOW)

  print("Waiting for echo rising edge")
  pulse_start = time.time()
  while GPIO.input(echo_pin) == GPIO.LOW:
    pulse_start = time.time()

  print("Waiting for echo falling edge")
  pulse_stop = time.time()
  while GPIO.input(echo_pin) == GPIO.LOW:
    pulse_stop = time.time()

# Distance = Time-of-Flight (in one direction) / Inverse of Sound Speed
  distance = (pulse_stop - pulse_start) * 34000 / 2

  if distance >= 200 or distance <= 0:
    print("Out of range")
  else:
    print("Distance (cm)", distance)

  time.sleep(1)

