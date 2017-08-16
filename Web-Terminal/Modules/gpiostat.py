#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Judge gpio status
"""

import RPi.GPIO as GPIO
import time

def gpio_status(GPIO_PIN):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN)
    if(GPIO.input(GPIO_PIN) == 1):
        return "on"
    else:
        return "off"
    GPIO.cleanup()

if __name__ == '__main__':
    GPIO_PIN = 12
    print gpio_status(GPIO_PIN)