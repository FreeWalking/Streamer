#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 16:39:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.input_link.url_stream import Ui_Dialog
import re


class Input_stream(QDialog, Ui_Dialog):
    """docstring for Input_name"""

    def __init__(self):
        super(Input_stream, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(open('static/style.qss').read())
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Отмена")
        self.buttonBox.accepted.connect(self.check_url)

    def check_url(self):
        reg = "http[s]?://"
        if re.match(reg, self.url_stream_le.text()) is None:
            QMessageBox.question(
                self, 'Message', "Ошибка! Введите адрес стрима в формате https://...", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication([])
    w = Input_name()
    w.show()
    app.exec_()
