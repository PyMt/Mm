import configparser
import os

__all__ = ['SSHvalue','Mailvalue']

class SSHvalue:
    def __init__(self):
        cp = configparser.ConfigParser()
        cp.sections()
        cp.read('./Config.ini')
        self.port = cp.getint("ssh", 'port')
        self.ip = cp['ssh']['ip']
        self.username = cp['ssh']['username']
        self.password = cp['ssh']['password']
        # self.cmd = cp['ssh']['cmd']

class Mailvalue:
    def __init__(self):
        cp = configparser.ConfigParser()
        cp.sections()
        cp.read('./Config.ini')
        self.mail_user = cp['mail']['mail_user']
        self.mail_host = cp['mail']['mail_host']
        self.mail_pass = cp['mail']['mail_pass']