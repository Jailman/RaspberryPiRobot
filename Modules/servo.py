#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Control servo
"""

import RPi.GPIO as GPIO
import time
import atexit
import sys



atexit.register(GPIO.cleanup)  

servopin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(1)


def run(angle):
    p.ChangeDutyCycle(angle)
    time.sleep(0.02)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print "Need an argument."
