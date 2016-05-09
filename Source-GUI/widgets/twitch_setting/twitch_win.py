# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twitch_set.ui'
#
# Created: Tue Apr 26 17:51:33 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Twitch_settings(object):
    def setupUi(self, Twitch_settings):
        Twitch_settings.setObjectName("Twitch_settings")
        Twitch_settings.resize(455, 335)
        self.verticalLayout = QtWidgets.QVBoxLayout(Twitch_settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Twitch_settings)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.nick_lineEdit = QtWidgets.QLineEdit(Twitch_settings)
        self.nick_lineEdit.setObjectName("nick_lineEdit")
        self.horizontalLayout.addWidget(self.nick_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(Twitch_settings)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.password_lineEdit = QtWidgets.QLineEdit(Twitch_settings)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Twitch_settings)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Twitch_settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Twitch_settings)
        self.buttonBox.accepted.connect(Twitch_settings.accept)
        self.buttonBox.rejected.connect(Twitch_settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Twitch_settings)

    def retranslateUi(self, Twitch_settings):
        _translate = QtCore.QCoreApplication.translate
        Twitch_settings.setWindowTitle(_translate("Twitch_settings", "Настройка Twitch"))
        self.label_3.setText(_translate("Twitch_settings", "Введите ваш ник на Twitch"))
        self.label_5.setText(_translate("Twitch_settings", "Введите QAuth token"))
        self.label_4.setText(_translate("Twitch_settings", "Для того чтобы получить OAuth token необходимо пройти по ссылке http://www.twitchapps.com/tmi/ и нажать кнопку Connect with Twitch. В появившемся окне появится токен, который необходимо будет ввести в поле выше. Например: oauth:ghgjhjkf8743hjhjk32 (токен вводится вместе с oauth:)"))

