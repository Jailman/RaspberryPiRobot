#!/usr/bin/python
# coding:utf-8
__author__ = 'Jailman'

import smtplib
from email.mime.text import MIMEText


class MailToWarn():

    def __init__(self, mailto_list, mail_host, mail_user, mail_pass):
        self.mailto_list = mailto_list
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass

    def send_mail(self, content):
        msg = MIMEText(content, _subtype='html', _charset='gb2312')
        msg['Subject'] = "RaspberryPi Robot Mailer"  # Email subject
        msg['From'] = self.mail_user
        # msg['To'] = self.mailto_list
        strTo = self.mailto_list
        msg['To'] = ','.join(strTo)

        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host)  # SMTP server
            s.login(self.mail_user, self.mail_pass)  # login
            s.sendmail(self.mail_user, self.mailto_list,
                       msg.as_string())  # sendmail
            s.close()
            return True
        except Exception, e:
            print str(e)
            return False

def Mailer(list, content):
    mail_host = 'smtp.sina.com'
    mail_user = 'xxx@sina.com'
    mail_pass = 'xxx'
    mailer = MailToWarn(list, mail_host, mail_user, mail_pass)
    if mailer.send_mail(content):
        print 'Success'
    else:
        print 'Fail'

if __name__ == '__main__':
    list = ['541197941@qq.com', 'jailman@sina.com']
    content = 'Test Mail'
    Mailer(list, content)
