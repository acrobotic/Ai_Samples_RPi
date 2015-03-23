# Install Python Module RPi.GPIO
#sudo apt-get update
#sudo apt-get install python-dev python-rpi.gpio

import RPi.GPIO as G
import time

relay_pin = 5 

G.setmode(G.BOARD)
G.setup(relay_pin,G.OUT)

# Need to wait for a bit until the 'setmode' has an effect.
# Weird, right?
time.sleep(1)

G.output(relay_pin,True)
time.sleep(5)
G.output(relay_pin, False)
G.cleanup()
