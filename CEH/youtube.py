#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import PyQt5
import PyQt5.QtCore
import PyQt5.QtWidgets as QT
import PyQt5.QAxContainer


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setMinimumSize(PyQt5.QtCore.QSize(650, 350))
        self.buttonBox = PyQt5.QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(PyQt5.QtCore.QRect(300, 170, 161, 32))
        self.buttonBox.setOrientation(PyQt5.QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(PyQt5.QtWidgets.QDialogButtonBox.Cancel|PyQt5.QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = PyQt5.QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(PyQt5.QtCore.QRect(220, 40, 351, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.videoDown = PyQt5.QtWidgets.QRadioButton(Dialog)
        self.videoDown.setGeometry(PyQt5.QtCore.QRect(240, 120, 121, 17))
        self.videoDown.setChecked(True)
        self.videoDown.setObjectName("videoDown")
        self.audioDown = PyQt5.QtWidgets.QRadioButton(Dialog)
        self.audioDown.setGeometry(PyQt5.QtCore.QRect(440, 120, 82, 17))
        self.audioDown.setChecked(False)
        self.audioDown.setObjectName("audioDown")
        self.urlPrompt = PyQt5.QtWidgets.QLabel(Dialog)
        self.urlPrompt.setGeometry(PyQt5.QtCore.QRect(40, 35, 161, 31))
        self.urlPrompt.setObjectName("urlPrompt")
        # self.frame.setGeometry(PyQt5.QtCore.QRect(50, 180, 191, 141))
        # self.frame.setAutoFillBackground(True)
        # self.frame.setFrameShape(PyQt5.QtWidgets.QFrame.WinPanel)
        # self.frame.setFrameShadow(PyQt5.QtWidgets.QFrame.Plain)
        # self.frame.setObjectName("frame")
        self.thumbNail = PyQt5.QtWidgets.QLabel(Dialog)
        self.thumbNail.setGeometry(PyQt5.QtCore.QRect(60, 143, 121, 20))
        self.thumbNail.setObjectName("thumbNail")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(Dialog)

        





    def retranslateUi(self, Dialog):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Youtube Video/Audio Assistant"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "youtube link here"))
        self.videoDown.setText(_translate("Dialog", "Download Video"))
        self.audioDown.setText(_translate("Dialog", "Audio Only"))
        self.urlPrompt.setText(_translate("Dialog", "Enter your youtube video link"))
        self.thumbNail.setText(_translate("Dialog", "Link Thumbnail Display"))
        Dialog.show()



