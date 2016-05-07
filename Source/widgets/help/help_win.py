# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_win.ui'
#
# Created: Wed Apr 27 14:17:45 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogHelp(object):
    def setupUi(self, DialogHelp):
        DialogHelp.setObjectName("DialogHelp")
        DialogHelp.resize(937, 580)
        DialogHelp.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogHelp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.help_treeWidget = QtWidgets.QTreeWidget(DialogHelp)
        self.help_treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.help_treeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.help_treeWidget.setAnimated(True)
        self.help_treeWidget.setAllColumnsShowFocus(False)
        self.help_treeWidget.setWordWrap(True)
        self.help_treeWidget.setColumnCount(1)
        self.help_treeWidget.setObjectName("help_treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.help_treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.help_treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.help_treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.help_treeWidget)
        self.help_textBrowser = QtWidgets.QTextBrowser(DialogHelp)
        self.help_textBrowser.setOpenExternalLinks(True)
        self.help_textBrowser.setObjectName("help_textBrowser")
        self.horizontalLayout.addWidget(self.help_textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogHelp)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogHelp)
        self.buttonBox.accepted.connect(DialogHelp.accept)
        self.buttonBox.rejected.connect(DialogHelp.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogHelp)

    def retranslateUi(self, DialogHelp):
        _translate = QtCore.QCoreApplication.translate
        DialogHelp.setWindowTitle(_translate("DialogHelp", "Справка"))
        self.help_treeWidget.headerItem().setText(0, _translate("DialogHelp", "Справка по программе"))
        __sortingEnabled = self.help_treeWidget.isSortingEnabled()
        self.help_treeWidget.setSortingEnabled(False)
        self.help_treeWidget.topLevelItem(0).setText(0, _translate("DialogHelp", "Введение"))
        self.help_treeWidget.topLevelItem(1).setText(0, _translate("DialogHelp", "Основное"))
        self.help_treeWidget.topLevelItem(1).child(0).setText(0, _translate("DialogHelp", "Интерфейс"))
        self.help_treeWidget.topLevelItem(1).child(1).setText(0, _translate("DialogHelp", "Меню"))
        self.help_treeWidget.topLevelItem(1).child(2).setText(0, _translate("DialogHelp", "Twitch - user/password"))
        self.help_treeWidget.topLevelItem(1).child(3).setText(0, _translate("DialogHelp", "Избранные"))
        self.help_treeWidget.topLevelItem(2).setText(0, _translate("DialogHelp", "Дополнительно"))
        self.help_treeWidget.topLevelItem(2).child(0).setText(0, _translate("DialogHelp", "Используемые библиотеки"))
        self.help_treeWidget.topLevelItem(2).child(1).setText(0, _translate("DialogHelp", "Сообщить об ошибке"))
        self.help_treeWidget.setSortingEnabled(__sortingEnabled)

