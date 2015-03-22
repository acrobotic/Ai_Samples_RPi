#!/usr/bin/env python3
# Raspberry Pi 2 HC-SR04 ultrasonic distance sensor demo
# with TXB108 level shifter
#
# HC-SR04 to TXB108 to RPi
# GND        GND       GND (6)
# ECHO       B2<->A2   GPIO27 (13)
# TRIG       B1<->A1   GPIO17 (11)
# VCC        VB        5V (2)
#            VA        3.3V (1)
#
# Note: datasheets recommend connecting GND before VCC.
#
import time
import RPi.GPIO as GPIO

class Ultrasonic(object):

  def __init__(self, pin_mode, trig_pin, echo_pin):
    self.trig_pin = trig_pin
    self.echo_pin = echo_pin
    GPIO.setmode(pin_mode)
    GPIO.setup(self.trig_pin, GPIO.OUT)
    GPIO.setup(self.echo_pin, GPIO.IN)
    GPIO.output(self.trig_pin, GPIO.LOW)
    time.sleep(3)

  def __exit__(self, type, value, traceback):
    GPIO.cleanup(self.trig_pin)
    GPIO.cleanup(self.echo_pin)

  def range_cm(self):
    GPIO.output(self.trig_pin, GPIO.HIGH)
    time.sleep(10/1000/1000)
    cutoff = time.time() + 0.60
    GPIO.output(self.trig_pin, GPIO.LOW)

    pulse_start = 0
    pulse_stop = 0
    while GPIO.input(self.echo_pin) == GPIO.LOW:
      pulse_start = time.time()
      if (pulse_start > cutoff):
        return None
    while GPIO.input(self.echo_pin) == GPIO.HIGH:
      pulse_stop = time.time()
      if (pulse_stop > cutoff):
        return None

    # Distance = Time-of-Flight (in one direction) / Inverse of Sound Speed
    distance = (pulse_stop - pulse_start) / 2 * 34000
    if distance >= 400 or distance <= 2:
      return None
    return distance

if __name__ == "__main__":
  import signal
  import sys
  def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)
  signal.signal(signal.SIGINT, signal_handler)

  ultrasonic = Ultrasonic(GPIO.BOARD,11,13)

  while True:
    distance = ultrasonic.range_cm()
    if distance:
      print("Distance %s cm" % distance)
    time.sleep(1)

