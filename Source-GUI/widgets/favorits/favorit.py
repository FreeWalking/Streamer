#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 16:39:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.favorits.favorit_win import Ui_DialogFavorit
import json
import re
from widgets.input_link import def_url
#from favorit_win import Ui_DialogFavorit


class Favorits(QDialog, Ui_DialogFavorit):
    """docstring for Favorits"""

    def __init__(self):
        super(Favorits, self).__init__()
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Save).setText("Сохранить")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Отмена")
        self.path = 'setting.json'
        self.setStyleSheet(open('static/style.qss').read())
        self.list_fav()
        self.plus_pb.setIcon(QIcon(":/icons/icons/plus.png"))
        self.minus_pb.setIcon(QIcon(":/icons/icons/minus.png"))
        self.plus_pb.clicked.connect(self.addfav)
        self.minus_pb.clicked.connect(self.delfav)

    def list_fav(self):
        try:
            self.data = json.load(open(self.path))
            for i in self.data['favorit']:
                self.favlist_listWidget.addItem(i)
        except FileNotFoundError:
            print("File with setting not found")
        except KeyError:
            self.data['favorit'] = []
            json.dump(self.data, open(self.path, 'w'))
            self.list_fav()

    def addfav(self):
        name = def_url.Input_stream()
        if name.exec_():
            link = name.url_stream_le.text()
            reg = "http[s]?://"
            if re.match(reg, link) is not None:
                self.data['favorit'].append(link)
                json.dump(self.data, open(self.path, 'w'))

            self.favlist_listWidget.clear()
            self.list_fav()

    def delfav(self):
        buf = self.favlist_listWidget.currentItem().text()
        self.data['favorit'].remove(buf)
        json.dump(self.data, open(self.path, 'w'))
        self.favlist_listWidget.clear()
        self.list_fav()


if __name__ == '__main__':
    app = QApplication([])
    w = Favorits()
    w.show()
    app.exec_()
