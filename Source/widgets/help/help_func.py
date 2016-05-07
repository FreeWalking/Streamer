#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-15 16:39:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from widgets.input_link.url_stream import Ui_Dialog
#from help_win import Ui_DialogHelp
from widgets.help.help_win import Ui_DialogHelp
import json
import os.path


class Help_class(QDialog, Ui_DialogHelp):
    """docstring for Help_class"""

    def __init__(self):
        super(Help_class, self).__init__()
        self.setupUi(self)
        self.path = 'widgets/help'
        self.setStyleSheet(open('style.qss').read())
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Выход")
        # self.create_help()
        self.help_treeWidget.itemPressed.connect(self.show_help)

    def create_help(self):
        a = ['Введение', 'Интерфейс', 'Меню', 'Twitch - user/password',
             'Избранные', 'Используемые библиотеки', 'Сообщить об ошибке']
        b = ['introduction', 'interface', 'menu',
             'twitch', 'favorit', 'library', 'send_error']
        data = dict(zip(a, b))
        json.dump(data, open('help_setting.json', 'w'), ensure_ascii=False)

    def show_help(self, item):
        print(item.text(0))
        data = json.load(open(os.path.join(self.path, 'help_setting.json')))
        for k, v in data.items():
            if item.text(0) == k:
                self.help_textBrowser.setSource(
                    QUrl(os.path.join(self.path, 'html/{}.html'.format(v))))


if __name__ == '__main__':
    app = QApplication([])
    w = Help_class()
    w.show()
    app.exec_()
