# -*- coding: utf-8 -*-
#!/usr/bin/python

from ModuleRegule import Regule
from Connect import connect
import json


class device_status(object):

    def __init__(self):
        _con = connect()
        _device_common = 'dis device' + '\n' + 'dis temperature all' + '\n'
        self.res = _con.ssh_result(_device_common)
        self.Status = Regule(self.res)
        self.menu = ['sub', 'type', 'online',
                     'power', 'register', 'status', 'Role']
        self.TemMenu = ['Sensor', 'Status', 'Current_Tem',
                        'Lower_Tem', 'Upper_Tem', 'UpperResume_Tem']

    def get_Fan(self):
        return dict(zip(self.menu, self.Status.FanStatus()))

    def get_Pwr(self):
        return dict(zip(self.menu, self.Status.PwrStatus()))

    def get_Switch(self):
        return dict(zip(self.menu, self.Status.SwitchStatus()))

    def Temperature(self):
        return dict(zip(self.TemMenu, self.Status.Temperature()))


if __name__ == "__main__":
    device_status = device_status()
    Fan_status = json.dumps(device_status.get_Fan(),
                            sort_keys=True, indent=4, separators=(',', ':'))
    Pwr_status = json.dumps(device_status.get_Pwr(),
                            sort_keys=True, indent=4, separators=(',', ':'))
    Switch_status = json.dumps(device_status.get_Switch(),
                            sort_keys=True, indent=4, separators=(',', ':'))
    temperature = json.dumps(device_status.Temperature(),
                            sort_keys=True, indent=4, separators=(',', ':'))
    print(Fan_status, Pwr_status, Switch_status, temperature)
