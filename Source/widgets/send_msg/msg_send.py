#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 16:39:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from msg_win import Ui_DialogMsgSend
from widgets.send_msg.msg_win import Ui_DialogMsgSend
import smtplib
from email.mime.text import MIMEText


class Msg_send(QDialog, Ui_DialogMsgSend):
    """docstring for Msg_send"""

    def __init__(self):
        super(Msg_send, self).__init__()
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Отправить")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Отмена")
        self.setStyleSheet(open('style.qss').read())
        self.show_msg()
        self.close()
        # self.buttonBox.accepted.connect(self.send_message)

    def show_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(
            "Извените, но данная функция не доступна в этой версии программы")
        msg.setWindowTitle("Error Sen Message")
        msg.exec_()

    def send_message(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    w = Msg_send()
    w.show()
    app.exec_()
