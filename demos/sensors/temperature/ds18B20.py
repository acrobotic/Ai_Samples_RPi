#!/usr/bin/env python
import os
from glob import glob   
from time import sleep 

base_dir = '/sys/bus/w1/devices/'
device_folder = glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return round(temp_c,2), round(temp_f,2)
	
while True:
	print("Temperature: %02.02f C %02.02f F" % read_temp())	
	sleep(1)

