#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 16:39:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.twitch_setting.twitch_win import Ui_Twitch_settings
# from twitch_win import Ui_Twitch_settings
import json
import base64


class Twitch_set(QDialog, Ui_Twitch_settings):
    """docstring for Twitch_set"""

    def __init__(self):
        super(Twitch_set, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(open('static/style.qss').read())
        self.buttonBox.button(QDialogButtonBox.Save).setText("Сохранить")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Отмена")
        self.dict_settings = {}
        self.file_get_userpass = True
        self.path = 'setting.json'
        self.buttonBox.accepted.connect(self.write_usepass)
        self.get_userpass()

    def get_userpass(self):
        try:
            self.dict_settings = json.load(open(self.path))
            self.nick_lineEdit.setText(self.dict_settings['Username'])
            userkey = self.dict_settings['Password']
            userkey = base64.b64decode(userkey)
            userkey = userkey.decode('utf-8')
            self.password_lineEdit.setText(userkey)
        except FileNotFoundError:
            print("Файл не найден")
        except KeyError:
            self.file_get_userpass = False
            print("In file settings user and pass not set(settings)")

    def write_usepass(self):
        user = self.nick_lineEdit.text()
        userkey = self.password_lineEdit.text()
        if user and userkey:
            self.dict_settings['Username'] = user
            userkey = base64.b64encode(bytes(userkey, "utf-8"))
            self.dict_settings['Password'] = userkey.decode('utf-8')
            json.dump(self.dict_settings, open(self.path, 'w'))

        else:
            print('Error! User and oauth token not saved')


if __name__ == '__main__':
    app = QApplication([])
    w = Twitch_set()
    w.show()
    app.exec_()
