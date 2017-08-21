#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
ultrasonic sensor
"""

import RPi.GPIO as GPIO
from driver import *
import time

chi = 23
cho = 22

def checkdist():
    #发出触发信号
    GPIO.output(cho, GPIO.HIGH)
    #保持10us以上（我选择15us）
    time.sleep(0.000015)
    GPIO.output(cho, GPIO.LOW)
    while not GPIO.input(chi):
        pass
    #发现高电平时开时计时
    t1 = time.time()
    while GPIO.input(chi):
        pass
    #高电平结束停止计时
    t2 = time.time()
    #返回距离，单位为米
    return (t2-t1)*340/2

def auto_pilot():
    GPIO.setmode(GPIO.BCM)
    #第15号针，GPIO22
    GPIO.setup(cho, GPIO.OUT, initial=GPIO.LOW)
    #第16号针，GPIO23
    GPIO.setup(chi, GPIO.IN)
    time.sleep(2)

    try:
        while True:
            dist = checkdist()
            if dist < 0.2:
                left()
                sleep(0.2)
            else:
                forward()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    auto_pilot()