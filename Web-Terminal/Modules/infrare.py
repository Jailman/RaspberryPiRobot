#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:23:08 2014

@author: pi
"""

# import smtplib
# from email.mime.text import MIMEText
import RPi.GPIO as gpio
# import MySQLdb as mdb
import time

# mail_to="*******@qq.com"
#
# def store_in_database(param):
#     conn=mdb.connect(host="localhost",user='root',passwd='******',db='sensor',charset='utf8')
#     cur=conn.cursor()
#     sql="insert into infrared_sensor(record_time,in_range) values(now(),'%s')"%param
#     cur.execute(sql)
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# def send_mail(to_list,title,content):
#     mail_host="smtp.126.com"
#     mail_user="*****"
#     mail_pass="******"
#     mail_postfix="126.com"
#     me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
#     msg=MIMEText(content)
#     msg['Subject']=title
#     msg['From']=mail_user
#     msg['To']=to_list
#
#     mail=smtplib.SMTP()
#     mail.connect(mail_host)
#     mail.login(mail_user,mail_pass)
#     mail.sendmail(me,to_list,msg.as_string())
#     mail.close()


def is_anybody_home():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(8, gpio.IN)
    if gpio.input(8) == 1:
        return 1
    else:
        return 0

# current_time="%d" % time.localtime().tm_hour+":"+ "%d" % time.localtime().tm_min


def main():
    if is_anybody_home() == 1:
        # send_mail(mail_to,"Is someone in sensor range?--"+current_time,"Yes--"+current_time)
        # param="Yes"
        # store_in_database(param)
        print 'There is somebody near!'
    else:
        # send_mail(mail_to,"Is someone in sensor range?--"+current_time,"No--"+current_time)
        # param="No"
        # store_in_database(param)
        print 'Nobody is near.'

if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
