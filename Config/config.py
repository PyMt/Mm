import configparser
import os

__all__ = ['SSHvalue']

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
