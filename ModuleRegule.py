# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import re

__all__ = ['Regule']

class Regule:
    def __init__(self, string):
        self.string = string

    def PwrStatus(self):
        pattern = re.compile(r'PWR1.*')
        listP = pattern.findall(self.string)[0][:-2].split()  # split以空格分词
        return listP

    def FanStatus(self):
        pattern = re.compile(r'FAN1.*')
        listF = pattern.findall(self.string)[0][:-2].split()
        return listF

    def SwitchStatus(self):
        pattern = re.compile(r'-.*S5730.*')
        listS = pattern.findall(self.string)[1][:-2].split()
        return listS

    def Temperature(self):
        pattern = re.compile(r'NA.*[0-9]')
        # listTem = pattern.findall(string)[2:][2:].split()
        listTem = pattern.findall(self.string)[0][6:].split()
        return listTem
