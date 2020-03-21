# -*- coding: utf-8 -*-
#!/usr/bin/python

from Config import config
import paramiko
import threading
import time
import os

__all__ = ['connect']


class connect:
    def __init__(self):
        value = config.SSHvalue()
        self.ip = value.ip
        self.port = value.port
        self.username = value.username
        self.password = value.password

    def ssh_result(self, cmd):
        t = paramiko.Transport(self.ip, self.port)
        t.connect(username=self.username, password=self.password)
        chan = t.open_session()
        chan.settimeout(timeout=15)
        chan.get_pty()
        chan.invoke_shell()
        time.sleep(5)
        i = 1
        while i < 10:
            chan.send(cmd)
            i += 1
        time.sleep(2)
        result = chan.recv(65535)
        result = str(result, encoding='utf-8')
        return result
