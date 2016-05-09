# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favorit.ui'
#
# Created: Tue Apr 26 16:54:14 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogFavorit(object):
    def setupUi(self, DialogFavorit):
        DialogFavorit.setObjectName("DialogFavorit")
        DialogFavorit.resize(551, 371)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogFavorit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogFavorit)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.favlist_listWidget = QtWidgets.QListWidget(DialogFavorit)
        self.favlist_listWidget.setObjectName("favlist_listWidget")
        self.verticalLayout.addWidget(self.favlist_listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plus_pb = QtWidgets.QPushButton(DialogFavorit)
        self.plus_pb.setMaximumSize(QtCore.QSize(50, 16777215))
        self.plus_pb.setText("")
        self.plus_pb.setFlat(True)
        self.plus_pb.setObjectName("plus_pb")
        self.horizontalLayout.addWidget(self.plus_pb)
        self.minus_pb = QtWidgets.QPushButton(DialogFavorit)
        self.minus_pb.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minus_pb.setText("")
        self.minus_pb.setFlat(True)
        self.minus_pb.setObjectName("minus_pb")
        self.horizontalLayout.addWidget(self.minus_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogFavorit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogFavorit)
        self.buttonBox.accepted.connect(DialogFavorit.accept)
        self.buttonBox.rejected.connect(DialogFavorit.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogFavorit)

    def retranslateUi(self, DialogFavorit):
        _translate = QtCore.QCoreApplication.translate
        DialogFavorit.setWindowTitle(_translate("DialogFavorit", "Избранные каналы"))
        self.label.setText(_translate("DialogFavorit", "Избранные"))
        self.favlist_listWidget.setSortingEnabled(True)

