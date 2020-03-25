#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from Config import config


__all__ = ['mail']


class mail:
    def __init__(self):
        value = config.Mailvalue()
        self.mail_user = value.mail_user
        self.mail_host = value.mail_host
        self.mail_pass = value.mail_pass

    def sendmail(self, receivers,context):
        sender = '631643983@qq.com'
        # receivers = ['fralychen@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        message = MIMEText(context, 'plain', 'utf-8')
        message['From'] = Header("info_center", 'utf-8')
        message['To'] = Header("administrator", 'utf-8')

        subject = 'Switch_info'
        message['Subject'] = Header(subject, 'utf-8')
        try:
           smtpObj = smtplib.SMTP()
           smtpObj.connect(self.mail_host, 25)    # 25 为 SMTP 端口号
           smtpObj.login(self.mail_user, self.mail_pass)
           smtpObj.sendmail(sender, receivers, message.as_string())
           print("邮件发送成功")
        except smtplib.SMTPException:
           print("Error: 无法发送邮件")
    
