#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-14 12:44:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
from PyQt5.QtCore import QThread
from time import sleep, ctime


class MyThread(QThread):
    """docstring for MyThread"""

    def __init__(self, func, args, name=''):
        super(MyThread, self).__init__()
        self.name = name
        self.args = args
        self.func = func

    def getResult(self):
        return self.res

    def run(self):
        print('startin', self.name, 'at:', ctime())
        #self.active = True
        # while self.active:
        #    try:
        self.res = self.func(*self.args)
        #    except Exception:
        #        continue

        print(self.name, 'fineshed at:', ctime())
