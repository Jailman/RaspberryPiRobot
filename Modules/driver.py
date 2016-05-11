#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import sys
from time import sleep

Channel_A = 31
Channel_B = 33
Channel_C = 35
Channel_D = 37


def init_driver():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Channel_A, GPIO.OUT)
    GPIO.setup(Channel_B, GPIO.OUT)
    GPIO.setup(Channel_C, GPIO.OUT)
    GPIO.setup(Channel_D, GPIO.OUT)

def stop():
    GPIO.output(Channel_A, GPIO.LOW)
    GPIO.output(Channel_B, GPIO.LOW)
    GPIO.output(Channel_C, GPIO.LOW)
    GPIO.output(Channel_D, GPIO.LOW)


def forward():
    stop()
    GPIO.output(Channel_A, GPIO.HIGH)
    GPIO.output(Channel_D, GPIO.HIGH)
#    sleep(1)
#    stop()

def backward():
    stop()
    GPIO.output(Channel_B, GPIO.HIGH)
    GPIO.output(Channel_C, GPIO.HIGH)
#    sleep(1)
#    stop()

def right():
    stop()
    GPIO.output(Channel_C, GPIO.HIGH)
    GPIO.output(Channel_A, GPIO.HIGH)
#    sleep(1)
#    stop()

def left():
    stop()
    GPIO.output(Channel_B, GPIO.HIGH)
    GPIO.output(Channel_D, GPIO.HIGH)
#    sleep(1)
#    stop()

if __name__ == '__main__':
    init_driver()
    if len(sys.argv) == 0:
        print "Usage: [forward|backward|stop|left|right]"
    if sys.argv[1] == "forward":
        forward()
    if sys.argv[1] == "backward":
        backward()
    if sys.argv[1] == "stop":
        stop()
    if sys.argv[1] == "left":
        left()
    if sys.argv[1] == "right":
        right()

