# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_win.ui'
#
# Created: Wed Apr 27 16:30:03 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogMsgSend(object):
    def setupUi(self, DialogMsgSend):
        DialogMsgSend.setObjectName("DialogMsgSend")
        DialogMsgSend.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogMsgSend)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DialogMsgSend)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogMsgSend)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogMsgSend)
        self.buttonBox.accepted.connect(DialogMsgSend.accept)
        self.buttonBox.rejected.connect(DialogMsgSend.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMsgSend)

    def retranslateUi(self, DialogMsgSend):
        _translate = QtCore.QCoreApplication.translate
        DialogMsgSend.setWindowTitle(_translate("DialogMsgSend", "Отпправить сообщение об ошибке"))

