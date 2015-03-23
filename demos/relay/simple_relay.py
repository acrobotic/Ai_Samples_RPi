# Install Python Module RPi.GPIO
#sudo apt-get update
#sudo apt-get install python-dev python-rpi.gpio

import RPi.GPIO as G
import time

G.setmode(G.BOARD)
G.setup(8,G.OUT)

# Need to wait for a bit until the 'setmode' has an effect.
# Weird, right?
time.sleep(1)


G.output(2,True)
time.sleep(2)
G.output(2, False)
G.cleanup()
