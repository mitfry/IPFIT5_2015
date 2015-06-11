# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Functions.ui'
#
# Created: Thu Jun 11 14:35:36 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(306, 237)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox_1 = QtGui.QCheckBox(Dialog)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.verticalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(Dialog)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(Dialog)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(Dialog)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtGui.QCheckBox(Dialog)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.verticalLayout.addWidget(self.checkBox_6)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.pushButton_1 = QtGui.QPushButton(Dialog)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.gridLayout_3.addWidget(self.pushButton_1, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Functions", None))
        self.checkBox_1.setText(_translate("Dialog", "Cloud", None))
        self.checkBox_2.setText(_translate("Dialog", "Email", None))
        self.checkBox_3.setText(_translate("Dialog", "Hardware", None))
        self.checkBox_4.setText(_translate("Dialog", "Hash", None))
        self.checkBox_5.setText(_translate("Dialog", "Internetgeschiedenis", None))
        self.checkBox_6.setText(_translate("Dialog", "Software", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_1.setText(_translate("Dialog", "Ok", None))

